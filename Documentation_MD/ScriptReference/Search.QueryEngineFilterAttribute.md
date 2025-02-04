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

# QueryEngineFilterAttribute

class in UnityEditor.Search

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

Base attribute class used to define a custom filter on a QueryEngine. All
filter types supported by QueryEngine.AddFilter are supported by this
attribute.

For a usage example, see
[QueryEngine.AddFiltersFromAttribute](Search.QueryEngine_1.AddFiltersFromAttribute.html).

### Properties

[comparisonOptions](Search.QueryEngineFilterAttribute-comparisonOptions.html)|
String comparison options.  
---|---  
[overridesStringComparison](Search.QueryEngineFilterAttribute-
overridesStringComparison.html)| Flag indicating if the filter overrides the
global string comparison options. Set to true when the comparisonOptions are
used.  
[paramTransformerFunction](Search.QueryEngineFilterAttribute-
paramTransformerFunction.html)| Name of the parameter transformer function to
use with this filter. Tag the parameter transformer function with the
appropriate ParameterTransformer attribute.  
[supportedOperators](Search.QueryEngineFilterAttribute-
supportedOperators.html)| List of supported operator tokens. Null for all
operators.  
[token](Search.QueryEngineFilterAttribute-token.html)| The identifier of the
filter. Typically what precedes the operator in a filter (i.e. "id" in
"id>=2").  
[useParamTransformer](Search.QueryEngineFilterAttribute-
useParamTransformer.html)| Flag indicating if this filter uses a parameter
transformer function. Set to true when paramTransformerFunction is used.  
[useRegularExpressionToken](Search.QueryEngineFilterAttribute-
useRegularExpressionToken.html)| Indicates if the filter uses a regular
expression token or not.  
  
### Constructors

[QueryEngineFilterAttribute](Search.QueryEngineFilterAttribute-ctor.html)|
Create a filter with the corresponding token and supported operators.  
---|---  
  
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

