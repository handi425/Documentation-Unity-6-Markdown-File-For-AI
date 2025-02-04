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

# SupportedOnRenderPipelineAttribute

class in UnityEngine.Rendering

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

Set which render pipelines make a class active.

Add `[SupportedOnRenderPipeline]` above a class to set which [Render Pipeline
Assets](Rendering.RenderPipelineAsset.html) make a class active. For example,
`[SupportedOnRenderPipeline(typeof(HDRenderPipelineAsset))`.  
  
`[SupportedOnRenderPipeline]` works only with some attributes - for example,
[CustomEditor](CustomEditor.html). You can use `[SupportedOnRenderPipeline]`
without an argument if you want all [Scriptable Render
Pipeline](../Manual/ScriptableRenderPipeline.html) Assets to make the class
active. The following example makes the `BehaviourEditor` class active when
any Scriptable Render Pipeline asset is active.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    [[CustomEditor](CustomEditor.html)(typeof([Behaviour](Behaviour.html)))]
    [SupportedOnRenderPipeline]
    public class BehaviourEditor : [Editor](Editor.html)
    {
        public override void OnInspectorGUI()
        {
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)($"{nameof(BehaviourEditor)} is supported on the currently active render pipeline.");
        }
    }  
      
    public class [Behaviour](Behaviour.html) : [MonoBehaviour](MonoBehaviour.html)
    {
    }
    

Additional resources:
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html).

### Properties

[isSupportedOnCurrentPipeline](Rendering.SupportedOnRenderPipelineAttribute-
isSupportedOnCurrentPipeline.html)| The value is true if the current
RenderPipelineAsset supports the attribute.  
---|---  
[renderPipelineTypes](Rendering.SupportedOnRenderPipelineAttribute-
renderPipelineTypes.html)| The Render Pipeline Assets that support the
attribute.  
  
### Public Methods

[GetSupportedMode](Rendering.SupportedOnRenderPipelineAttribute.GetSupportedMode.html)|
Use SupportedOnRenderPipelineAttribute.GetSupportedMode to find out whether a
RenderPipelineAsset supports the attribute.  
---|---  
  
### Static Methods

[IsTypeSupportedOnRenderPipeline](Rendering.SupportedOnRenderPipelineAttribute.IsTypeSupportedOnRenderPipeline.html)|
Use this method to determine whether a type has the
SupportedOnRenderPipelineAttribute attribute and determine whether a
RenderPipelineAsset type supports that attribute.  
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

