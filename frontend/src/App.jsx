import React, { useState } from 'react';
import P2PSwap from './components/P2PSwap';
import MerchantQR from './components/MerchantQR';
import TransactionHistory from './components/TransactionHistory';

export default function App() {
  const [connected, setConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState(null);
  const [view, setView] = useState('p2p'); // p2p, merchant, history

  const connectWallet = async () => {
    // TODO: Implement TON Connect wallet integration here
    setWalletAddress('0xExampleWalletAddress123');
    setConnected(true);
  };

  const renderView = () => {
    switch(view) {
      case 'p2p':
        return <P2PSwap />;
      case 'merchant':
        return <MerchantQR />;
      case 'history':
        return <TransactionHistory />;
      default:
        return <P2PSwap />;
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>TON Mini-App: P2P Payments & Merchant QR</h1>
      {!connected ? (
        <button onClick={connectWallet}>Connect Wallet via TON Connect</button>
      ) : (
        <>
          <p>Wallet connected: {walletAddress}</p>
          <nav>
            <button onClick={() => setView('p2p')}>P2P Swap</button>
            <button onClick={() => setView('merchant')}>Merchant QR</button>
            <button onClick={() => setView('history')}>Transaction History</button>
          </nav>
          <div style={{ marginTop: 20 }}>
            {renderView()}
          </div>
        </>
      )}
    </div>
  );
}
