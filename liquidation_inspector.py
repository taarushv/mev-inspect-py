import json
from typing import Optional

from web3 import Web3

from typing import List, Optional

from mev_inspect import utils
from mev_inspect.config import load_config
from mev_inspect.schemas.blocks import NestedTrace, TraceType
from mev_inspect.schemas.classifications import Classification
from mev_inspect.schemas.strategy import Strategy, Liquidation

from .base import StrategyInspector

class LiquidationInspector(StrategyInspector):

	def __init__(self):
		self.result = []

	# Inspect list of classified traces and identify liquidation
	def inspect(self, traces):

		event = []

		# For each trace
		for i in range(1, len(traces)):
			trace = traces[i]

			# Liquidation condition
			if trace.classification == Classification.liquidate:

				# Collateral data from the liquidation.
				# The inputs will differ by DEX, this is AAVE

				for i in trace.inputs:
					if( i["name"] == '_purchaseAmount'):
						value = trace.inputs[i]
					elif (i["name"] == '_collateral'):
						collateral_type = trace.inputs[i]
					elif (i["name"] == '_reserve'):
						collateral_source = trace.inputs[i]


				# Define the address of the liquidator
				liquidator = trace.from_address

				# Find a transfer before liquidation with a to_address corresponding to the liquidator
				for trace in traces[:i]:
					if (trace.classification == Classification.transfer & trace.to_address == liquidator):
						profit = 
						#Calculate profit


				# Tag liquidation
				event.append(Strategy(strategy=StategyType.liquidation,
									  traces=[trace],
									  protocols=[trace.protocol]))


		return result
