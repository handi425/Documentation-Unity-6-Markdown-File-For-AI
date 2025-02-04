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

# RendererListParams

struct in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Struct holding the arguments that are needed to create a renderers
[RendererList](Rendering.RendererList.html).

### Static Properties

[Invalid](Rendering.RendererListParams.Invalid.html)| Returns an empty
RendererListParams.  
---|---  
  
### Properties

[cullingResults](Rendering.RendererListParams-cullingResults.html)| The set of
visible objects to draw. You typically obtain this from
ScriptableRenderContext.Cull.  
---|---  
[drawSettings](Rendering.RendererListParams-drawSettings.html)| A struct that
describes how to draw the objects.  
[filteringSettings](Rendering.RendererListParams-filteringSettings.html)| A
struct that describes how to filter the set of visible objects, so that Unity
only draws a subset.  
[isPassTagName](Rendering.RendererListParams-isPassTagName.html)| If set to
true, tagName specifies a Pass Tag. Otherwise, tagName specifies a SubShader
Tag.  
[stateBlocks](Rendering.RendererListParams-stateBlocks.html)| An array of
structs that describe which parts of the GPU's render state to override.  
[tagName](Rendering.RendererListParams-tagName.html)| The name of a SubShader
Tag or Pass Tag.  
[tagValues](Rendering.RendererListParams-tagValues.html)| An array of
ShaderTagId structs, where the name is the value of a given SubShader Tag or
Pass Tag.  
  
### Constructors

[RendererListParams](Rendering.RendererListParams-ctor.html)| Create a
RendererListParams struct.  
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

