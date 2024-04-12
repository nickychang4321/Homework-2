# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> profitable path : tokenB-\>tokenA-\>tokenD-\>tokenC-\>tokenB\
> amountIn : 5 ether\
> amountOut : 20 ether\
> final reward : 20.129888944077443 

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> 滑點是指預期交易價格與實際執行價格之間的差異\
> Uniswap V2 引入slippage tolerance，允許使用者在兌換過程中設定一個可接受的價格偏差比例。當兌換價格超出這個偏差比例時，交易就會失败。\

```solidity
function swap(address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOutMin, address to) public virtual {
  // ... (other swap logic)

  // 检查实际兑换到的代幣數量是否少於容許的最小值
  uint256 amountOut =getAmountOut(amountIn, tokenIn, tokenOut);
  require(amountOut >= amountOutMin, 'Uniswap: Insufficient output amount');

  // ... (transfer tokens)
}
```

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> 是為了防止流動性池中出現過小的流動性，從而保證了交易對的流動性水平足夠，並防止惡意操縱。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> 確保向流動性池中注入資金的方式是按照一定的規則進行，可以降低市場中的滑點和操縱風險，提高交易的效率和公平性。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> sandwich attack 會在偵測到其他人購買貨幣時，搶先在他之前購買，造成增加滑點，使受害者購買的價格變高，攻擊者可以以較高的價格出售。

