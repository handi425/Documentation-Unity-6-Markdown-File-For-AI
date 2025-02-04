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

# MinMaxGradient

struct in UnityEngine

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

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

### Description

Script interface for a Min-Max Gradient.

This contains two [Gradient](Gradient.html)s, and returns a
[Color](Color.html) based on
[ParticleSystem.MinMaxGradient.mode](ParticleSystem.MinMaxGradient-mode.html).
Depending on the mode, this may return the value randomized. Gradients are
edited via the ParticleSystem Inspector once a
[ParticleSystemGradientMode](ParticleSystemGradientMode.html) requiring them
has been selected. Some modes do not require gradients, only colors.
Additional resources: [ParticleSystem](ParticleSystem.html).

    
    
    using UnityEngine;  
      
    // This example shows setting a constant color value.
    public class ConstantColorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.ColorOverLifetimeModule](ParticleSystem.ColorOverLifetimeModule.html) colorModule;  
      
        void Start()
        {
            // Get the system and the color module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            colorModule = myParticleSystem.colorOverLifetime;  
      
            GetValue();
            SetValue();
        }  
      
        void GetValue()
        {
            print("The constant color is " + colorModule.color.color);
        }  
      
        void SetValue()
        {
            colorModule.color = [Color.red](Color-red.html);
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows using 2 colors to drive the color over lifetime.
    public class TwoConstantColorsExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.ColorOverLifetimeModule](ParticleSystem.ColorOverLifetimeModule.html) colorModule;  
      
        void Start()
        {
            // Get the system and the color module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            colorModule = myParticleSystem.colorOverLifetime;  
      
            GetValue();
            SetValue();
        }  
      
        void GetValue()
        {
            print(string.Format("The constant values are: min {0} max {1}.", colorModule.color.colorMin, colorModule.color.colorMax));
        }  
      
        void SetValue()
        {
            colorModule.color = new [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)([Color.green](Color-green.html), [Color.red](Color-red.html));
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows using a gradient to drive the color over lifetime.
    public class GradientColorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.ColorOverLifetimeModule](ParticleSystem.ColorOverLifetimeModule.html) colorModule;
        [Gradient](Gradient.html) ourGradient;  
      
        void Start()
        {
            // Get the system and the color module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            colorModule = myParticleSystem.colorOverLifetime;  
      
            // A simple 2 color gradient with a fixed alpha of 1.0f.
            float alpha = 1.0f;
            ourGradient = new [Gradient](Gradient.html)();
            ourGradient.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) },
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(alpha, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(alpha, 1.0f) }
            );  
      
            // Apply the gradient.
            colorModule.color = ourGradient;  
      
            // In 5 seconds we will modify the gradient.
            Invoke("ModifyGradient", 5.0f);
        }  
      
        void ModifyGradient()
        {
            // Reduce the alpha
            float alpha = 0.5f;
            ourGradient.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) },
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(alpha, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(alpha, 1.0f) }
            );  
      
            // Apply the changed gradient.
            colorModule.color = ourGradient;
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows using 2 gradients to drive the color over lifetime.
    public class TwoGradientColorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.ColorOverLifetimeModule](ParticleSystem.ColorOverLifetimeModule.html) colorModule;  
      
        [Gradient](Gradient.html) ourGradientMin;
        [Gradient](Gradient.html) ourGradientMax;  
      
        void Start()
        {
            // Get the system and the emission module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            colorModule = myParticleSystem.colorOverLifetime;  
      
            // A simple 2 color gradient with a fixed alpha of 1.0f.
            float alpha1 = 1.0f;
            ourGradientMin = new [Gradient](Gradient.html)();
            ourGradientMin.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) },
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(alpha1, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(alpha1, 1.0f) }
            );  
      
            // A simple 2 color gradient with a fixed alpha of 0.0f.
            float alpha2 = 0.0f;
            ourGradientMax = new [Gradient](Gradient.html)();
            ourGradientMax.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) },
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(alpha2, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(alpha2, 1.0f) }
            );  
      
            // Apply the gradients.
            colorModule.color = new [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)(ourGradientMin, ourGradientMax);  
      
            // In 5 seconds we will modify the gradient.
            Invoke("ModifyGradient", 5.0f);
        }  
      
        void ModifyGradient()
        {
            // Reduce the alpha
            float alpha = 0.5f;
            ourGradientMin.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) },
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(alpha, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(alpha, 1.0f) }
            );  
      
            // Apply the changed gradients.
            colorModule.color = new [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)(ourGradientMin, ourGradientMax);
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows how to retrieve existing color and alpha keys from a [MinMaxGradient](ParticleSystem.MinMaxGradient.html)
    public class ReadGradientExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Get the system and the color module.
            var myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var colorModule = myParticleSystem.colorOverLifetime;  
      
            // Get the gradient (assuming the [MinMaxGradient](ParticleSystem.MinMaxGradient.html) is in [Gradient](Gradient.html) mode)
            [Gradient](Gradient.html) gradient = colorModule.color.gradient;  
      
            // Get the keys
            [GradientColorKey](GradientColorKey.html)[] colorKeys = gradient.colorKeys;
            [GradientAlphaKey](GradientAlphaKey.html)[] alphaKeys = gradient.alphaKeys;
        }
    }
    

### Properties

[color](ParticleSystem.MinMaxGradient-color.html)| Set a constant color.  
---|---  
[colorMax](ParticleSystem.MinMaxGradient-colorMax.html)| Set a constant color
for the upper bound.  
[colorMin](ParticleSystem.MinMaxGradient-colorMin.html)| Set a constant color
for the lower bound.  
[gradient](ParticleSystem.MinMaxGradient-gradient.html)| Set the gradient.  
[gradientMax](ParticleSystem.MinMaxGradient-gradientMax.html)| Set a gradient
for the upper bound.  
[gradientMin](ParticleSystem.MinMaxGradient-gradientMin.html)| Set a gradient
for the lower bound.  
[mode](ParticleSystem.MinMaxGradient-mode.html)| Set the mode that the Min-Max
Gradient uses to evaluate colors.  
  
### Constructors

[ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient-ctor.html)| A
single constant color for the entire gradient.  
---|---  
  
### Public Methods

[Evaluate](ParticleSystem.MinMaxGradient.Evaluate.html)| Manually query the
gradient to calculate colors based on what mode it is in.  
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

