import { useEffect, useMemo, useState } from 'react'
import axios, { AxiosResponse } from 'axios'
import './App.css'

axios.defaults.baseURL = 'http://localhost:9000/api/v1/'

interface Bill extends Record<string, number> {}

function App() {
  const [bill, setBill] = useState<Bill>({})
  const [is_individual_payment, setIsIndividual] = useState<boolean>(false)
  const hasValues = useMemo(() => !!Object.keys(bill).length, [bill])
  const total = useMemo(() => Object.values(bill).reduce((acc, value) => acc + value, 0), [bill])

  
  useEffect(() => {
    getBill(is_individual_payment)
  }, [is_individual_payment])

  function getBill(is_individual_payment: boolean) {
    axios.get('orders/calculate-total', { params: { is_individual_payment } }).then((response: AxiosResponse<Bill>) => {
      setBill(response.data)
    })
  }

  function payBill() {
    axios.post('orders/pay', { is_individual_payment }).then(() => {
      setBill({})
    })
  }

  function FriendBill() {
    return Object.entries(bill).map(([name, amount]) => {
      return (
        <li className='bill-item' key={name}>
          <span>{name}</span>
          <span>${amount}</span>
        </li>
      )
    
    })
  }

  function Resume() {
    return (
      <div>
          <div className="is-individual">
            <label>
              <input
                type="checkbox"
                checked={!is_individual_payment}
                onChange={() => setIsIndividual(!is_individual_payment)}
                />
                <span>Pagar en partes iguales</span>
            </label>
          </div>
          <ul className="bill-list">
            <FriendBill />
          </ul>
          <button onClick={payBill}>Pagar: ${total}</button>
        </div>
    )
  }

  return (
    <>
      <div>
        {hasValues ? <Resume /> : <div>Sin ordenes :)</div>}
      </div>
    </>
  )
}

export default App
