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

#
[AssetPostprocessor](AssetPostprocessor.html).OnPostprocessGameObjectWithAnimatedUserProperties(GameObject,
EditorCurveBinding[])

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

### Parameters

gameObject | The GameObject with animated custom properties.  
---|---  
bindings | The animation curves bound to the custom properties.  
  
### Description

This function is called when the animation curves for a custom property are
finished importing.

It is called for every GameObject with an animated custom property. Each
animated property has an animation curve that is represented by an
[EditorCurveBinding](EditorCurveBinding.html). This lets you dynamically add
components to a GameObject and retarget the EditorCurveBindings to any
animatable property.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class MyAllPostprocessor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPostprocessGameObjectWithAnimatedUserProperties([GameObject](GameObject.html) go, [EditorCurveBinding](EditorCurveBinding.html)[] bindings)
        {
            // add a particle emitter to every game object that has a custom property called "particleAmount"
            // then map the animation to the emission rate
            for (int i = 0; i < bindings.Length; i++)
            {
                if (bindings[i].propertyName == "particlesAmount")
                {
                    [ParticleSystem](ParticleSystem.html) emitter = go.AddComponent<[ParticleSystem](ParticleSystem.html)>();
                    var emission = emitter.emission;
                    emission.rateOverTimeMultiplier = 0;  
      
                    bindings[i].propertyName = "EmissionModule.rateOverTime.scalar";
                    bindings[i].path = [AnimationUtility.CalculateTransformPath](AnimationUtility.CalculateTransformPath.html)(go.transform, go.transform.root);
                    bindings[i].type = typeof([ParticleSystem](ParticleSystem.html));
                }
            }
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

