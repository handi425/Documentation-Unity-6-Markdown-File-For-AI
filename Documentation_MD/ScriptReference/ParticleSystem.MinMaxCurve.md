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

# MinMaxCurve

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

Script interface for a Min-Max Curve.

Min-Max Curve. describes functions which take a value between a minimum and
maximum limit and return a value based on
[ParticleSystem.MinMaxCurve.mode](ParticleSystem.MinMaxCurve-mode.html).
Depending on the mode, this may return randomized values. For modes that
require curves, the value returned is dependent on one or two curves designed
in the ParticleSystem Inspector, that can be evaluated to a single value
between -n and n, where n is a constant also set in the Inspector. See
[ParticleSystemCurveMode](ParticleSystemCurveMode.html) for more information.  
  
Additional resources: [ParticleSystem](ParticleSystem.html).

    
    
    using UnityEngine;  
      
    // This example shows setting a constant rate value.
    public class ConstantRateExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.EmissionModule](ParticleSystem.EmissionModule.html) emissionModule;  
      
        void Start()
        {
            // Get the system and the emission module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            emissionModule = myParticleSystem.emission;  
      
            GetValue();
            SetValue();
        }  
      
        void GetValue()
        {
            print("The constant value is " + emissionModule.rateOverTime.constant);
        }  
      
        void SetValue()
        {
            emissionModule.rateOverTime = 10.0f;
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows using 2 constants to drive the rate.
    public class TwoConstantsRateExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.EmissionModule](ParticleSystem.EmissionModule.html) emissionModule;  
      
        void Start()
        {
            // Get the system and the emission module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            emissionModule = myParticleSystem.emission;  
      
            GetValue();
            SetValue();
        }  
      
        void GetValue()
        {
            print(string.Format("The constant values are: min {0} max {1}.", emissionModule.rateOverTime.constantMin, emissionModule.rateOverTime.constantMax));
        }  
      
        void SetValue()
        {
            emissionModule.rateOverTime = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.0f, 10.0f);
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows using a curve to drive the rate.
    public class CurveRateExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.EmissionModule](ParticleSystem.EmissionModule.html) emissionModule;  
      
        // We can "scale" the curve with this value. It gets multiplied by the curve.
        public float scalar = 1.0f;  
      
        [AnimationCurve](AnimationCurve.html) ourCurve;  
      
        void Start()
        {
            // Get the system and the emission module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            emissionModule = myParticleSystem.emission;  
      
            // A simple linear curve.
            ourCurve = new [AnimationCurve](AnimationCurve.html)();
            ourCurve.AddKey(0.0f, 0.0f);
            ourCurve.AddKey(1.0f, 1.0f);  
      
            // Apply the curve.
            emissionModule.rateOverTime = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(scalar, ourCurve);  
      
            // In 5 seconds we will modify the curve.
            Invoke("ModifyCurve", 5.0f);
        }  
      
        void ModifyCurve()
        {
            // Add a key to the current curve.
            ourCurve.AddKey(0.5f, 0.0f);  
      
            // Apply the changed curve.
            emissionModule.rate = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(scalar, ourCurve);
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows using 2 curves to drive the rate.
    public class TwoCurveRateExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) myParticleSystem;
        [ParticleSystem.EmissionModule](ParticleSystem.EmissionModule.html) emissionModule;  
      
        [AnimationCurve](AnimationCurve.html) ourCurveMin;
        [AnimationCurve](AnimationCurve.html) ourCurveMax;  
      
        // We can "scale" the curves with this value. It gets multiplied by the curves.
        public float scalar = 1.0f;  
      
        void Start()
        {
            // Get the system and the emission module.
            myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            emissionModule = myParticleSystem.emission;  
      
            // A horizontal straight line at value 1.
            ourCurveMin = new [AnimationCurve](AnimationCurve.html)();
            ourCurveMin.AddKey(0.0f, 1.0f);
            ourCurveMin.AddKey(1.0f, 1.0f);  
      
            // A horizontal straight line at value 0.5.
            ourCurveMax = new [AnimationCurve](AnimationCurve.html)();
            ourCurveMax.AddKey(0.0f, 0.5f);
            ourCurveMax.AddKey(1.0f, 0.5f);  
      
            // Apply the curves.
            emissionModule.rateOverTime = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(scalar, ourCurveMin, ourCurveMax);  
      
            // In 5 seconds we will modify the curve.
            Invoke("ModifyCurve", 5.0f);
        }  
      
        void ModifyCurve()
        {
            // Create a "pinch" point.
            ourCurveMin.AddKey(0.5f, 0.7f);
            ourCurveMax.AddKey(0.5f, 0.6f);  
      
            // Apply the changed curve.
            emissionModule.rateOverTime = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(scalar, ourCurveMin, ourCurveMax);
        }
    }
    
    
    
    using UnityEngine;  
      
    // This example shows how to retrieve existing keys from a [MinMaxCurve](ParticleSystem.MinMaxCurve.html)
    public class ReadCurveExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Get the system and the emission module.
            var myParticleSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var emissionModule = myParticleSystem.emission;  
      
            // Get the curve (assuming the [MinMaxCurve](ParticleSystem.MinMaxCurve.html) is in Curve mode)
            [AnimationCurve](AnimationCurve.html) curve = emissionModule.rateOverTime.curve;  
      
            // Get the keys
            [Keyframe](Keyframe.html)[] keys = curve.keys;
        }
    }
    

### Properties

[constant](ParticleSystem.MinMaxCurve-constant.html)| Set the constant value.  
---|---  
[constantMax](ParticleSystem.MinMaxCurve-constantMax.html)| Set a constant for
the upper bound.  
[constantMin](ParticleSystem.MinMaxCurve-constantMin.html)| Set a constant for
the lower bound.  
[curve](ParticleSystem.MinMaxCurve-curve.html)| Set the curve.  
[curveMax](ParticleSystem.MinMaxCurve-curveMax.html)| Set a curve for the
upper bound.  
[curveMin](ParticleSystem.MinMaxCurve-curveMin.html)| Set a curve for the
lower bound.  
[curveMultiplier](ParticleSystem.MinMaxCurve-curveMultiplier.html)| Set a
multiplier to apply to the curves.  
[mode](ParticleSystem.MinMaxCurve-mode.html)| Set the mode that the min-max
curve uses to evaluate values.  
  
### Constructors

[ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve-ctor.html)| A single
constant value for the entire curve.  
---|---  
  
### Public Methods

[Evaluate](ParticleSystem.MinMaxCurve.Evaluate.html)| Manually query the curve
to calculate values based on what mode it is in.  
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

