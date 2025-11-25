import React, { useState } from 'react';

export default function MerchantQR() {
  const [amount, setAmount] = useState('');
  const [qrData, setQrData] = useState(null);

  const generateQR = () => {
    // TODO: Integrate with backend /merchant/qr API
    // For now, simulate QR data string
    setQrData(`merchant:example_merchant;amount:${amount}`);
  };

  return (
    <div>
      <h2>Merchant QR Payment</h2>
      <div>
        <label>Amount (INR/USDC):</label>
        <input
          type="number"
          min="0"
          step="0.01"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <button onClick={generateQR}>Generate QR</button>
      </div>
      {qrData && (
        <div style={{ marginTop: '20px' }}>
          <p>QR Data:</p>
          <code>{qrData}</code>
          {/* TODO: Replace with actual QR code rendering */}
        </div>
      )}
    </div>
  );
}
