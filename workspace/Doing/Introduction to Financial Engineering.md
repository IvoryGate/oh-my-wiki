---
title: Introduction to Financial Engineering
type: note
created: 2026-09-17
updated: 2026-09-17
status: doing
tags:
  - 主题/经济与金融
---
# Introduction to Financial Engineering

## Interest Rate Theory, Cash Flow Analysis, and Bonds

### Interest Rate Theory

**Time Value of Money**

> Interest is the result of the time value of money.

Money received today generally more valuabe than the amout of money received in the future, becasue money available today can earn interest.

For example, if the interest rate is 10% per year, $\$100$ today will become
$$
100 \times (1 + 10\%) = 110
$$
one year later.

Therefore, $\$100$ today is equivalent to $\$110$ one year later.

So, cash flows occurring at different points in time are not directly comparable. To compare them, we need to convert their values to the same point in time using an appropriate interest rate. This is the basic idea behind present value analysis.

> 货币具有时间价值，在比较不同时间的货币的价值，不能直接比较金额，应该通过 interest rate 转化到同一个时间点进行比较。

**Compounding Frequency**

Banks may calculate and pay interest more frequently than once a year - for example, quarterly, monthly, or daily. However, the interest rate is usually still quoted on an annual basis.

Suppose the annualized interest rate is $r$ and interest is compounded $m$ times per year.

- simple interest - $A \rightarrow A(1+r)$
- compounding interest - $A \rightarrow A(1+\frac{r}{4})^4$

**Annualized Interest Rate vs. Effective Annual Interest Rate**

**Annualized Interest Rate**

The **annualized interest rate** is the quoted annual rate $r$.

For example, $r=12\%$

with monthly compounding means that the monthly interest rate is
$$
\frac{12\%}{12}=1\%
$$
The annualized rate itself is still $r=12\%$.

**Effective annual interest rate**

The effective annual interest rate measures the actual percentage increase in wealth over one year after taking compounding into account.

If there are $m$ compounding periods per year,
$$
A \rightarrow A(1+\frac rm)^m
$$
after one year.

Therefore,
$$
r_{effective} = (1+\frac rm)^m - 1
$$

> Annualized rate 是“报价利率”，effective annual rate 是一年下来实际增长的部分，因为复利的存在，后者通常比前者高。

**Continue Compouding**

when the number of compounding periods becomes infinitely large:
$$
m\to\infty
$$

$$
\left(1+\frac rm\right)^m\to e^r
$$

Therefore, under **continuous compounding**, an initial amount $A$ grows to

$Ae^r$ after one year.

The corresponding effective annual interest rate is $e^r-1$.

when 

- Cash flow
- cash flow stream

### Cash Flow Analysis

$$
\text{Cash Flow} \rightarrow \text{Present Value} \rightarrow \text{Compare Investments} \rightarrow \text{IRR}
$$

> 先表示现金流，再将不同时间的现金流折算到同一个时间点，最后进行投资比较。

**Cash Flow and Cash Flow Stream**

A cash flow is a net receipt at some time. For example, $+\$100$ means a cash inflow of $\$100$, while $-\$50$ means a cash outflow of $\$50$.

A cash flow stream is a series of flows over several periods. We usually write it as $(x_0,x_1,\ldots,x_n)$, where $x_k$ represents the cash flow at time $k$. For example, $(-100,30,40,50)$.

**Present Value**

As mentioned above, money at different points in time is not directly comparable. The same applies to cash flows. Therefore, we convert future cash flows into their equivalent values at the present time.

For a future cash flow \(X\) at time \(n\),
$$
PV=\frac{X}{(1+r)^n}.
$$
For a cash flow stream,
$$
PV=x_0+\frac{x_1}{1+r}+\cdots+\frac{x_n}{(1+r)^n}.
$$
**Present Value Analysis**

Choose the investment with the higher present value:
$$
PV(x)\geq PV(y).
$$
All cash flows associated with the investment, both profit and cost, should be included.

**Internal Rate of Return**

The Internal rate of return (IRR) of a cash flow stream $(x_0,x_1,\ldots,x_n)$ is the interest rate $r$ such that
$$
0=x_0+\frac{x_1}{1+r}+\cdots+\frac{x_n}{(1+r)^n}.
$$
It is the discount rate that makes the present value of the cash flow stream equal to zero.

**Internal Rate of Return Analysis**

Economically, IRR can be interpreted as the **break-even rate of return** of the investment. At the IRR, the present value of future cash inflows exactly offsets the present value of the cash outflows.

For a conventional investment, if the required return is lower than the IRR, the investment has a positive present value; if the required return is higher than the IRR, the investment has a negative present value.

Therefore, IRR can be used to evaluate an investment by comparing the investment's implied rate of return with the required or market rate of return.



### Annuity 与 Loan Analysis

**Annuity**

**Bonds**

> 发行人承诺按照事先约定的规则，未来向债券持有人支付钱。到期时会支付面值（face value / par value），很多债券还会定期支付票息（coupon）。

### Duration & Interest Rate Risk

### Immunization

### Dynamic Programming

### Valuation of a Firm

### Free Cash Flow, FCF

