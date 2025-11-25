import React from 'react';

const mockTransactions = [
  { id: 1, type: 'P2P Swap', amount: 50, status: 'Completed', date: '2024-06-01' },
  { id: 2, type: 'Merchant Payment', amount: 20, status: 'Pending', date: '2024-06-03' },
];

export default function TransactionHistory() {
  return (
    <div>
      <h2>Transaction History</h2>
      <table border="1" cellPadding="5" cellSpacing="0">
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Amount (USDC)</th>
            <th>Status</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {mockTransactions.map((txn) => (
            <tr key={txn.id}>
              <td>{txn.id}</td>
              <td>{txn.type}</td>
              <td>{txn.amount}</td>
              <td>{txn.status}</td>
              <td>{txn.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
