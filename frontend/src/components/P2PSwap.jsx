import React, { useState } from 'react';

export default function P2PSwap() {
  const [receiver, setReceiver] = useState('');
  const [amount, setAmount] = useState('');
  const [message, setMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    // TODO: Integrate with backend /p2p/swap API
    setMessage(`P2P swap request to ${receiver} for ${amount} USDC sent.`);
  };

  return (
    <div>
      <h2>P2P USDC Swap</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Receiver Telegram Username:</label>
          <input
            type="text"
            value={receiver}
            onChange={(e) => setReceiver(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Amount (USDC):</label>
          <input
            type="number"
            min="0"
            step="0.01"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />
        </div>
        <button type="submit">Initiate Swap</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
