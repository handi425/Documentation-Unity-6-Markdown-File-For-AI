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

#  [RenderingLayerMask](RenderingLayerMask.html).GetMask

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

public static uint GetMask(params string[] renderingLayerNames);

### Parameters

renderingLayerNames | List of layer names to convert to a rendering layer mask.  
---|---  
  
### Returns

**uint** The rendering layer mask created from the `renderingLayerNames`.

### Description

Given a set of rendering layer names as defined in the [Tags and Layers
manager](../Manual/class-TagManager.html), returns the equivalent rendering
layer mask for all of them.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)([RenderingLayerMask.GetMask](RenderingLayerMask.GetMask.html)("UserLayerA", "UserLayerB"));
        }
    }
    

**Note:** Suppose `UserLayerA` and `UserLayerB` are the tenth and eleventh
layers. These will have a Rendering Layer values of 10 and 11. To obtain their
layer mask value their names can be passed into
[GetMask](RenderingLayerMask.GetMask.html). The argument can either be a list
of their names or an array of strings storing their names. In this case the
return value will be 2^10 + 2^11 = 3072.

* * *

## Declaration

public static uint GetMask(ReadOnlySpan<string> renderingLayerNames);

### Parameters

renderingLayerNames | Span of layer names to convert to a rendering layer mask.  
---|---  
  
### Returns

**uint** The rendering layer mask created from the `renderingLayerNames`.

### Description

Given a set of rendering layer names as defined in the [Tags and Layers
manager](../Manual/class-TagManager.html), returns the equivalent rendering
layer mask for all of them.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)] string[] renderingLayerNames = { "UserLayerA", "UserLayerB" };  
      
        void Start()
        {
            [Debug.Log](Debug.Log.html)([RenderingLayerMask.GetMask](RenderingLayerMask.GetMask.html)(new ReadOnlySpan<string>(renderingLayerNames)));
        }
    }
    

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

