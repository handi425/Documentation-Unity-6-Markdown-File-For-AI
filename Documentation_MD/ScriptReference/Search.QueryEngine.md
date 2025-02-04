[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# QueryEngine

class in UnityEditor.Search

/

Inherits from:[Search.QueryEngine_1](Search.QueryEngine_1.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

A QueryEngine defines how to build a query from an input string. It can be
customized to support custom filters and operators. Default query engine of
type object.

See [QueryEngine<T>](Search.QueryEngine_1.html).

### Constructors

[QueryEngine](Search.QueryEngine-ctor.html)| Construct a new QueryEngine.  
---|---  
  
### Inherited Members

### Properties

[globalStringComparison](Search.QueryEngine_1-globalStringComparison.html)|
Global string comparison options for word matching and filter handling (if not
overridden).  
---|---  
[searchDataCallback](Search.QueryEngine_1-searchDataCallback.html)| The
callback used to get the data to match to the search words.  
[searchDataOverridesStringComparison](Search.QueryEngine_1-searchDataOverridesStringComparison.html)|
Indicates if word/phrase matching uses searchDataStringComparison or not.  
[searchDataStringComparison](Search.QueryEngine_1-searchDataStringComparison.html)|
String comparison options for word/phrase matching.  
[searchWordMatcher](Search.QueryEngine_1-searchWordMatcher.html)| The function
used to match the search data against the search words.  
[skipIncompleteFilters](Search.QueryEngine_1-skipIncompleteFilters.html)|
Boolean. Indicates if incomplete filters should be skipped. If true, filters
are skipped. If false and validateFilters is true, incomplete filters will
generate errors when parsed.  
[skipUnknownFilters](Search.QueryEngine_1-skipUnknownFilters.html)| Boolean.
Indicates if unknown filters should be skipped. If true, unknown filters are
skipped. If false and validateFilters is true, unknown filters will generate
errors if no default filter handler is provided.  
[validateFilters](Search.QueryEngine_1-validateFilters.html)| Get or set if
the engine must validate filters when parsing the query. Defaults to true.  
  
### Public Methods

[AddFilter](Search.QueryEngine_1.AddFilter.html)| Adds a new custom filter.  
---|---  
[AddFiltersFromAttribute](Search.QueryEngine_1.AddFiltersFromAttribute.html)|
Adds all custom filters that are identified with the method attribute
TFilterAttribute.  
[AddNestedQueryAggregator](Search.QueryEngine_1.AddNestedQueryAggregator.html)|
Adds a new nested query aggregator. An aggregator is an operation that can be
applied on a nested query to aggregate the results of the nested query
according to certain criteria.  
[AddOperator](Search.QueryEngine_1.AddOperator.html)| Adds a custom filter
operator.  
[AddOperatorHandler](Search.QueryEngine_1.AddOperatorHandler.html)| Adds a
custom filter operator handler.  
[AddTypeParser](Search.QueryEngine_1.AddTypeParser.html)| Adds a type parser
that parses a string and returns a custom type. Used by custom operator
handlers (see AddOperatorHandler).  
[ClearFilters](Search.QueryEngine_1.ClearFilters.html)| Removes all filters
that were added on the QueryEngine.  
[GetAllFilters](Search.QueryEngine_1.GetAllFilters.html)| Get all filters
added on this QueryEngine.  
[GetOperator](Search.QueryEngine_1.GetOperator.html)| Get a custom operator
added on the QueryEngine.  
[ParseQuery](Search.QueryEngine_1.ParseQuery.html)| Parses a query string into
a ParsedQuery operation. This ParsedQuery operation can then be used to filter
any data set of type TData.  
[RemoveFilter](Search.QueryEngine_1.RemoveFilter.html)| Removes a custom
filter.  
[RemoveOperator](Search.QueryEngine_1.RemoveOperator.html)| Removes a custom
operator that was added on the QueryEngine.  
[SetDefaultFilter](Search.QueryEngine_1.SetDefaultFilter.html)| Sets the
default filter handler for filters that were not registered.  
[SetDefaultParamFilter](Search.QueryEngine_1.SetDefaultParamFilter.html)| Sets
the default filter handler for function filters that were not registered.  
[SetFilterNestedQueryTransformer](Search.QueryEngine_1.SetFilterNestedQueryTransformer.html)|
Sets a filter's nested query transformer function. This function takes the
result of a nested query and extracts the necessary data to compare with the
filter.  
[SetGlobalStringComparisonOptions](Search.QueryEngine_1.SetGlobalStringComparisonOptions.html)|
Sets global string comparison options. Used for word matching and filter
handling (unless overridden by filter).  
[SetNestedQueryHandler](Search.QueryEngine_1.SetNestedQueryHandler.html)| Sets
the function that will handle nested queries. Only one handler can be set.  
[SetSearchDataCallback](Search.QueryEngine_1.SetSearchDataCallback.html)| Sets
the callback used to fetch the data that is matched against the search words.  
[SetSearchWordMatcher](Search.QueryEngine_1.SetSearchWordMatcher.html)| Set
the search word matching function to be used instead of the default one. Set
to null to use the default.  
[TryGetFilter](Search.QueryEngine_1.TryGetFilter.html)| Get a filter by its
token.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

