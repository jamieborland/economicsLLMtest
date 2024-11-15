#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:54:37 2024

@author: jamie
"""
import csv

test_data = [
    # Supply and Demand
    ("How do changes in consumer preferences impact demand for goods?", 
     "Shifts in consumer preferences can increase or decrease demand, affecting prices and market equilibrium."),
    
    ("What effect does a supply shock have on equilibrium price?", 
     "A supply shock, such as a sudden shortage, generally raises equilibrium prices as supply is restricted."),
    
    ("How do substitute goods influence the demand for a product?", 
     "The availability of substitutes can lower demand for a product, as consumers may switch to cheaper alternatives."),
    
    ("What is the impact of government subsidies on supply?", 
     "Subsidies lower production costs, often leading to increased supply and reduced market prices."),
    
    ("How does consumer income elasticity affect luxury goods?", 
     "High income elasticity means luxury goods are more responsive to income changes, with demand rising as incomes increase."),
    
    ("Why might a surplus occur in a market, and what are the effects?", 
     "A surplus occurs when supply exceeds demand, usually causing prices to drop as suppliers try to sell excess inventory."),
    
    ("How does price elasticity of demand influence revenue?", 
     "Inelastic demand means price increases lead to higher revenue, while elastic demand may reduce revenue as prices rise."),
    
    # Capital Markets and Investment
    ("How do interest rates affect bond prices in capital markets?", 
     "Bond prices typically move inversely to interest rates; as rates rise, existing bond prices fall."),
    
    ("What role does investor confidence play in stock market volatility?", 
     "Investor confidence influences stock prices, as optimism can drive up prices while fear causes sell-offs."),
    
    ("How does foreign investment affect domestic capital markets?", 
     "Foreign investment brings additional funds, often increasing liquidity and growth in domestic markets."),
    
    ("Why might companies choose equity financing over debt?", 
     "Equity financing doesn’t require regular interest payments and reduces financial risk, although it dilutes ownership."),
    
    ("What impact do central bank policies have on capital investment?", 
     "Central bank policies, like interest rate changes, influence borrowing costs and can encourage or discourage investment."),
    
    ("How does inflation affect returns on long-term investments?", 
     "Inflation erodes the real value of returns, making inflation-adjusted returns lower for long-term investments."),
    
    ("What is the significance of liquidity in capital markets?", 
     "Liquidity allows investors to quickly buy or sell assets, making markets more efficient and attractive to participants."),
    
    ("How do government bonds influence national debt levels?", 
     "Issuing government bonds raises debt, but also funds spending without immediate tax increases."),
    
    ("Why might low interest rates encourage riskier investments?", 
     "Low rates reduce returns on safe assets, leading investors to seek higher returns in riskier investments."),
    
    ("What is the effect of economic downturns on capital flows?", 
     "Downturns often lead to reduced capital flows as investors pull back or seek safer investments.")
]
test_data += [
    # Labor Markets and Employment
    ("How do changes in labor market demand influence wages?", 
     "Increased demand for labor generally raises wages, while decreased demand can lead to wage reductions."),
    
    ("What is the effect of technological advancements on labor markets?", 
     "Technological advancements can reduce demand for certain jobs while creating new opportunities in other areas."),
    
    ("Why might labor unions influence wage structures?", 
     "Labor unions negotiate higher wages and better conditions, impacting wage structures for unionized sectors."),
    
    ("How does minimum wage legislation affect part-time employment?", 
     "Minimum wage laws can reduce part-time job availability as businesses adjust to increased labor costs."),
    
    ("What role does workforce training play in reducing unemployment?", 
     "Training improves worker skills, increasing employability and reducing structural unemployment."),
    
    ("How do government job programs influence labor markets?", 
     "Government job programs can reduce unemployment by providing temporary positions and skill-building opportunities."),
    
    ("Why might flexible working hours attract a diverse workforce?", 
     "Flexible hours appeal to a wider range of workers, including those with caregiving responsibilities or other commitments."),
    
    # Public Debt and Fiscal Policy
    ("How does high public debt impact a country's economic policies?", 
     "High debt limits fiscal flexibility, constraining a country's ability to respond to economic challenges."),
    
    ("What is the effect of budget deficits on future tax policies?", 
     "Budget deficits often necessitate future tax increases or spending cuts to balance public finances."),
    
    ("How do government bonds relate to fiscal sustainability?", 
     "Issuing bonds raises funds for spending but also adds to national debt, affecting fiscal sustainability."),
    
    ("Why might public debt influence exchange rates?", 
     "High debt can reduce confidence in a currency, leading to depreciation as investors seek safer assets."),
    
    ("What role do automatic stabilizers play in fiscal policy?", 
     "Automatic stabilizers, like unemployment benefits, help cushion the economy during downturns without new policies."),
    
    ("How does the debt-to-GDP ratio signal economic health?", 
     "A high debt-to-GDP ratio indicates heavy borrowing, which may be unsustainable and hinder economic stability."),
    
    ("Why might austerity measures be implemented during fiscal crises?", 
     "Austerity reduces government spending, aiming to balance budgets and restore fiscal stability."),
    
    ("What is the impact of debt servicing on government spending priorities?", 
     "Debt servicing redirects funds from programs to interest payments, reducing available resources for other priorities."),
    
    ("How do fiscal stimulus packages affect short-term economic growth?", 
     "Fiscal stimulus boosts short-term growth by increasing spending, often financed through debt or tax cuts."),
    
    ("Why might sovereign debt influence a country's borrowing costs?", 
     "High debt levels increase borrowing costs as lenders demand higher returns to compensate for risk.")
]

test_data += [
    # Trade Policy and Globalization
    ("What is the impact of trade barriers on global supply chains?", 
     "Trade barriers disrupt supply chains, leading to higher costs and potential delays in production."),
    
    ("How does globalization affect income inequality within countries?", 
     "Globalization can widen income inequality as some sectors benefit more than others, leading to wage disparities."),
    
    ("Why might free trade agreements influence environmental policies?", 
     "Free trade agreements often include environmental clauses, encouraging countries to adopt higher standards."),
    
    ("What is the effect of tariffs on domestic industries?", 
     "Tariffs protect domestic industries by making imported goods more expensive, encouraging local production."),
    
    ("How do international trade agreements impact local economies?", 
     "Trade agreements open markets for local businesses but can also increase competition, impacting smaller industries."),
    
    ("Why might protectionist policies limit economic growth?", 
     "Protectionism reduces access to international markets, limiting growth opportunities for domestic industries."),
    
    ("How does globalization facilitate technology transfer?", 
     "Globalization allows countries to adopt new technologies from abroad, boosting productivity and innovation."),
    
    # Monetary Policy and Inflation
    ("What is the role of central banks in controlling inflation?", 
     "Central banks adjust interest rates and influence the money supply to maintain price stability."),
    
    ("How does inflation impact the purchasing power of consumers?", 
     "Inflation erodes purchasing power, as rising prices reduce the amount consumers can buy with a given income."),
    
    ("Why might interest rate hikes slow down economic growth?", 
     "Higher interest rates increase borrowing costs, reducing consumer spending and business investment."),
    
    ("What is the effect of inflation expectations on wage negotiations?", 
     "If inflation is expected to rise, workers may demand higher wages to maintain their purchasing power."),
    
    ("How does monetary policy impact foreign exchange rates?", 
     "Higher interest rates can attract foreign investment, leading to currency appreciation and impacting trade."),
    
    ("Why might deflation be harmful to an economy?", 
     "Deflation reduces consumer spending as people anticipate lower prices, potentially leading to economic stagnation."),
    
    ("What is the impact of quantitative easing on financial markets?", 
     "Quantitative easing injects liquidity into markets, lowering interest rates and stimulating investment."),
    
    ("How do supply-side inflation and demand-side inflation differ?", 
     "Supply-side inflation is driven by higher production costs, while demand-side inflation results from increased demand."),
    
    ("Why might central banks target a low but positive inflation rate?", 
     "A low inflation target promotes stability, preventing deflation and encouraging steady economic growth."),
    
    ("What is the effect of inflation on interest rates for savings?", 
     "Higher inflation generally leads to higher nominal interest rates to maintain positive real returns for savers.")
]

test_data += [
    # Taxation and Economic Incentives
    ("How do progressive taxes impact income redistribution?", 
     "Progressive taxes redistribute income by taxing higher earners more heavily, potentially reducing inequality."),
    
    ("What is the effect of tax deductions on consumer spending?", 
     "Tax deductions increase disposable income, which can encourage higher levels of consumer spending."),
    
    ("How do high corporate taxes influence business location decisions?", 
     "High corporate taxes may discourage businesses from locating in certain regions, impacting job creation."),
    
    ("Why might high consumption taxes discourage spending?", 
     "High consumption taxes raise the cost of goods, reducing purchasing power and potentially lowering demand."),
    
    ("What is the impact of capital gains tax cuts on wealth accumulation?", 
     "Capital gains tax cuts improve after-tax returns, encouraging investment and wealth accumulation."),
    
    ("How do estate taxes influence family-owned business succession?", 
     "Estate taxes can make succession costly, sometimes requiring family businesses to sell assets to pay the tax."),
    
    ("Why might tax incentives for green technology support environmental goals?", 
     "Tax incentives lower the cost of adopting green technology, encouraging sustainable practices and reducing emissions."),
    
    ("What is the effect of high income taxes on labor supply?", 
     "High income taxes reduce take-home pay, which may discourage people from working more hours or seeking higher wages."),
    
    ("How do payroll taxes impact small businesses?", 
     "Payroll taxes increase the cost of employment, which can limit small businesses' ability to hire or expand."),
    
    ("Why might lower taxes on capital gains encourage investment?", 
     "Lower capital gains taxes increase after-tax returns, making investments in stocks or property more attractive."),
    
    # Regulation and Economic Efficiency
    ("What is the impact of zoning laws on urban development?", 
     "Zoning laws restrict where buildings can be constructed, which can limit housing supply and increase prices."),
    
    ("How do labor regulations affect employment opportunities?", 
     "Labor regulations can raise costs, which may reduce hiring or limit job growth in certain industries."),
    
    ("Why might relaxed environmental regulations boost industrial output?", 
     "Relaxed regulations reduce compliance costs, potentially allowing industries to produce more at lower costs."),
    
    ("What is the effect of deregulation on competition in the telecommunications industry?", 
     "Deregulation opens the market to new players, increasing competition and potentially lowering prices."),
    
    ("How do banking regulations influence financial stability?", 
     "Banking regulations, like capital requirements, aim to ensure stability by reducing the risk of financial crises."),
    
    ("Why might high regulatory compliance costs reduce small business formation?", 
     "High compliance costs make it expensive to start a business, which may deter potential entrepreneurs."),
    
    ("What is the role of antitrust laws in promoting market competition?", 
     "Antitrust laws prevent monopolies, fostering competition and protecting consumer choice."),
    
    ("How do safety regulations impact production costs in manufacturing?", 
     "Safety regulations require protective measures, which can increase production costs for manufacturers."),
    
    ("Why might regulatory burdens decrease innovation in certain sectors?", 
     "Excessive regulations can limit flexibility, discouraging businesses from experimenting with new ideas or technologies."),
    
    ("What is the effect of relaxed trade regulations on import prices?", 
     "Relaxed trade regulations reduce barriers, often lowering import prices and increasing market competition.")
]

with open('data/neoclassical_test_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["prompt", "response"])
    writer.writerows(test_data)
