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

# TransformOrigin

struct in UnityEngine.UIElements

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Represents the point of origin where the transformations
([Scale](UIElements.Scale.html), [Translate](UIElements.Translate.html), and
[Rotate](UIElements.Rotate.html)) are applied.

By default, transform-origin is set in percentages relative to the element's
size. For example, 50% 50% sets the origin to the center of the element. These
percentages are calculated based on the element’s resulting layout size
(resolvedStyle.height and resolvedStyle.width). You can also specify
transform-origin in pixels. The origin is determined based on the local
coordinate system of the element, where the top-left corner is considered the
origin point (0,0) regardless of whether you use percentages or pixels.
Negative values and values larger than 100% are valid and move the transform-
origin outside the element.

### Constructors

[TransformOrigin](UIElements.TransformOrigin-ctor.html)|  
---|---  
  
### Static Methods

[Initial](UIElements.TransformOrigin.Initial.html)|  Returns the initial value
for the TransformOrigin property.  
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

