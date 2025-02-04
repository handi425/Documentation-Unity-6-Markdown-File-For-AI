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

# ParsedQuery<T0>

class in UnityEditor.Search

/

Inherits from:[Search.ParsedQuery_2](Search.ParsedQuery_2.html)

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

Provides methods to define an operation that can be used to filter a data set.

<T>: The filtered data type.

### Properties

[returnPayloadIfEmpty](Search.ParsedQuery_1-returnPayloadIfEmpty.html)|
Boolean. Indicates if the original payload should be returned when the query
is empty.  
---|---  
  
### Public Methods

[Apply](Search.ParsedQuery_1.Apply.html)| Applies the filtering on an
IEnumerable data set.  
---|---  
[Test](Search.ParsedQuery_1.Test.html)| Tests the query on a single object.
Returns true if the test passes.  
  
### Inherited Members

### Properties

[errors](Search.ParsedQuery_2-errors.html)| A list of QueryErrors.  
---|---  
[evaluationGraph](Search.ParsedQuery_2-evaluationGraph.html)| Query evaluation
graph used to evaluate the query.  
[queryGraph](Search.ParsedQuery_2-queryGraph.html)| Query graph. This graph
can be used to walk all the node of the query if you need to do a special type
of evaluation.  
[text](Search.ParsedQuery_2-text.html)| The text that generated the query.  
[tokens](Search.ParsedQuery_2-tokens.html)| The list of tokens found in the
query.  
[valid](Search.ParsedQuery_2-valid.html)| Indicates if the query is valid or
not.  
  
### Public Methods

[Apply](Search.ParsedQuery_2.Apply.html)| Applies the filtering on a payload.  
---|---  
[GetNodeAtPosition](Search.ParsedQuery_2.GetNodeAtPosition.html)| Get the
query node located at the specified index position in the query.  
[Optimize](Search.ParsedQuery_2.Optimize.html)| Optimizes the query by
optimizing the underlying filtering graph.  
  
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

