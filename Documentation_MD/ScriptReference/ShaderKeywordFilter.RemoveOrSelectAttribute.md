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

# RemoveOrSelectAttribute

class in UnityEditor.ShaderKeywordFilter

/

Inherits
from:[ShaderKeywordFilter.FilterAttribute](ShaderKeywordFilter.FilterAttribute.html)

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

Either remove or include the specified shader keywords in the build, depending
on the data field underneath.

Unity does the following in all `multi_compile` keyword sets:

  * Removes `keywordNames` if the data field under `RemoveOrSelect` matches the value of `condition`.
  * Includes only `keywordNames` if the data field under `RemoveOrSelect` does not match the value of `condition`.

    
    
    using UnityEditor.ShaderKeywordFilter;  
      
    [RemoveOrSelect(false, keywordNames: "FeatureA")]
    bool hasFeatureA;

Additional resources:
[FilterAttribute](ShaderKeywordFilter.FilterAttribute.html).

### Constructors

[RemoveOrSelectAttribute](ShaderKeywordFilter.RemoveOrSelectAttribute-
ctor.html)| Either remove or include the specified shader keywords in the
build, depending on the data field underneath.  
---|---  
  
### Inherited Members

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

