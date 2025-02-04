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

#  [UQueryExtensions](UIElements.UQueryExtensions.html).Q

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

## Declaration

public static T Q([UIElements.VisualElement](UIElements.VisualElement.html) e,
string name, params string[] classes);

### Parameters

e | Root VisualElement on which the selector will be applied.  
---|---  
name | If specified, will select elements with this name.  
classes | If provided, it selects elements with the specified class (case sensitive, to be distinguished from Type).  
  
### Returns

**T** The first element matching all the criteria, or null if none was found.

### Description

Convenience overload, shorthand for
[Query()](UIElements.UQueryExtensions.Query.html).[Build()](UQueryBuilder_1.Build.html).[First()](UQueryBuilder_1.First.html)

* * *

## Declaration

public static [UIElements.VisualElement](UIElements.VisualElement.html)
Q([UIElements.VisualElement](UIElements.VisualElement.html) e, string name,
params string[] classes);

### Parameters

e | Root VisualElement on which the selector will be applied.  
---|---  
name | If specified, will select elements with this name.  
classes | If provided, it selects elements with the specified class (case sensitive, to be distinguished from Type).  
  
### Returns

**VisualElement** The first element matching all the criteria, or null if none
was found.

### Description

Convenience overload, shorthand for
[Query()](UIElements.UQueryExtensions.Query.html).[Build()](UQueryBuilder_1.Build.html).[First()](UQueryBuilder_1.First.html)

* * *

## Declaration

public static T Q([UIElements.VisualElement](UIElements.VisualElement.html) e,
string name, string className);

### Parameters

e | Root VisualElement on which the selector will be applied.  
---|---  
name | If specified, will select elements with this name.  
className | If provided, it selects elements with the specified class (case sensitive, to be distinguished from Type).  
  
### Returns

**T** The first element matching all the criteria, or null if none was found.

### Description

Convenience overload, shorthand for
[Query()](UIElements.UQueryExtensions.Query.html).[Build()](UQueryBuilder_1.Build.html).[First()](UQueryBuilder_1.First.html)

* * *

## Declaration

public static [UIElements.VisualElement](UIElements.VisualElement.html)
Q([UIElements.VisualElement](UIElements.VisualElement.html) e, string name,
string className);

### Parameters

e | Root VisualElement on which the selector will be applied.  
---|---  
name | If specified, will select elements with this name.  
className | If provided, it selects elements with the specified class (case sensitive, to be distinguished from Type).  
  
### Returns

**VisualElement** The first element matching all the criteria, or null if none
was found.

### Description

Convenience overload, shorthand for `Query<T>.Build().First().`

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

