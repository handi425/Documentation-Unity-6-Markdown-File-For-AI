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
[ParticleSystem.CustomDataModule](ParticleSystem.CustomDataModule.html).SetMode

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

## Declaration

public void SetMode([ParticleSystemCustomData](ParticleSystemCustomData.html)
stream, [ParticleSystemCustomDataMode](ParticleSystemCustomDataMode.html)
mode);

### Parameters

stream | The name of the custom data stream to enable data generation on.  
---|---  
mode | The type of data to generate.  
  
### Description

Choose the type of custom data to generate for the chosen data stream.

Additional resources:
[ParticleSystem.CustomDataModule.GetMode](ParticleSystem.CustomDataModule.GetMode.html),
[ParticleSystem.GetCustomParticleData](ParticleSystem.GetCustomParticleData.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var customData = ps.customData;
            customData.enabled = true;  
      
            [Gradient](Gradient.html) grad = new [Gradient](Gradient.html)();
            grad.SetKeys(new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.blue](Color-blue.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) }, new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(0.0f, 1.0f) });  
      
            customData.SetMode([ParticleSystemCustomData.Custom1](ParticleSystemCustomData.Custom1.html), [ParticleSystemCustomDataMode.Color](ParticleSystemCustomDataMode.Color.html));
            customData.SetColor([ParticleSystemCustomData.Custom1](ParticleSystemCustomData.Custom1.html), grad);  
      
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            curve.AddKey(0.0f, 0.0f);
            curve.AddKey(1.0f, 1.0f);  
      
            customData.SetMode([ParticleSystemCustomData.Custom2](ParticleSystemCustomData.Custom2.html), [ParticleSystemCustomDataMode.Vector](ParticleSystemCustomDataMode.Vector.html));
            customData.SetVectorComponentCount([ParticleSystemCustomData.Custom2](ParticleSystemCustomData.Custom2.html), 1);
            customData.SetVector([ParticleSystemCustomData.Custom2](ParticleSystemCustomData.Custom2.html), 0, new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.0f, curve));
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

