# TON Mini-App Development Plan - P2P Payments & Merchant QR

## Phase 1: Backend API development
- [ ] Enhance backend/app/main.py to include:
  - P2P USDC swap endpoints with escrow contract interaction stubs
  - Merchant QR code generation and payment confirmation endpoints
  - Telegram WebApp API identity verification endpoint
- [ ] Create backend/app/models.py:
  - Define SQLAlchemy models for Users, Transactions, Disputes, and Merchants
- [ ] Create backend/app/escrow.py:
  - Implement smart contract escrow interaction logic for P2P swaps
- [ ] Create backend/app/telegram_auth.py:
  - Implement Telegram WebApp API identity verification logic

## Phase 2: Frontend UI development
- [ ] Expand frontend/src/App.jsx to scaffold the main app UI layout
- [ ] Create React components for:
  - P2P USDC swap flows (initiate, confirm, dispute)
  - Merchant QR code display and scanning interface
  - Wallet connection via TON Connect SDK integration
  - Transaction history and dispute handling UI
- [ ] Update frontend/package.json as needed for TON Connect and QR libraries

## Phase 3: DevOps and Integration
- [ ] Update Dockerfile and backend/start.sh to run backend and frontend
- [ ] Integrate backend APIs with frontend UI flows
- [ ] Add environment variables and configuration management

## Phase 4: Testing and Documentation
- [ ] Add unit and integration tests for backend endpoints and smart contract integration
- [ ] Add frontend component tests
- [ ] Write README.md usage and setup documentation

---

This phased plan provides a clear structure to complete the TON Mini-App as described in the pitch deck.
