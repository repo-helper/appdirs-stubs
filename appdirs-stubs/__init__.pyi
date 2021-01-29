#!/usr/bin/env python3
#
#  __init__.py
"""
Type stubs for appdirs
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright © 2016 Sebastian Meßmer <https://github.com/smessmer>
#    See https://github.com/ActiveState/appdirs/pull/75
#  Copyright © 2010 ActiveState Software Inc.
#    https://github.com/ActiveState/appdirs
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
from typing import Optional

def user_data_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		roaming: bool = ...,
		) -> str: ...

def site_data_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		multipath: bool = ...,
		) -> str: ...

def user_config_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		roaming: bool = ...,
		) -> str: ...

def site_config_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		multipath: bool = ...,
		) -> str: ...

def user_cache_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		opinion: bool = ...,
		) -> str: ...

def user_state_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		roaming: bool = ...,
		) -> str: ...

def user_log_dir(
		appname: Optional[str] = ...,
		appauthor: Optional[str] = ...,
		version: Optional[str] = ...,
		opinion: bool = ...,
		) -> str: ...

class AppDirs:

	def __init__(
			self,
			appname: Optional[str] = ...,
			appauthor: Optional[str] = ...,
			version: Optional[str] = ...,
			roaming: bool = ...,
			multipath: bool = ...,
			) -> None: ...

	@property
	def user_data_dir(self) -> str: ...

	@property
	def site_data_dir(self) -> str: ...

	@property
	def user_config_dir(self) -> str: ...

	@property
	def site_config_dir(self) -> str: ...

	@property
	def user_cache_dir(self) -> str: ...

	@property
	def user_state_dir(self) -> str: ...

	@property
	def user_log_dir(self) -> str: ...
