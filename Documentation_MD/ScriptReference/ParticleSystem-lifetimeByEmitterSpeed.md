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

#  [ParticleSystem](ParticleSystem.html).lifetimeByEmitterSpeed

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

public
[ParticleSystem.LifetimeByEmitterSpeedModule](ParticleSystem.LifetimeByEmitterSpeedModule.html)
lifetimeByEmitterSpeed;

### Description

Script interface for the Particle System Lifetime By Emitter Speed module.

This module controls the initial lifetime of each particle based on the speed
of the emitter when the particle was spawned.  
  
Particle System modules do not need to be reassigned back to the system; they
are interfaces and not independent objects.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool moduleEnabled = true;
        public float maxSpeed = 5.0f;
        public [AnimationCurve](AnimationCurve.html) curve = [AnimationCurve.EaseInOut](AnimationCurve.EaseInOut.html)(0.0f, 1.0f, 1.0f, 0.2f);  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var mainModule = ps.main;
            mainModule.startLifetime = 1.0f;  
      
            // make particles less random to more clearly see effect of lifetime.
            var shapeModule = ps.shape;
            shapeModule.radius = 0.1f;
            shapeModule.angle = 1.0f;  
      
            var main = ps.main;
            main.simulationSpace = [ParticleSystemSimulationSpace.World](ParticleSystemSimulationSpace.World.html);  
      
            // add a sphere so we can see our transform position as it moves
            var sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            sphere.transform.parent = ps.transform;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var lifetimeByEmitterSpeed = ps.lifetimeByEmitterSpeed;
            lifetimeByEmitterSpeed.enabled = moduleEnabled;
            lifetimeByEmitterSpeed.range = new [Vector2](Vector2.html)(0, maxSpeed);
            lifetimeByEmitterSpeed.curve = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1f, curve);  
      
            ps.transform.position = new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html) * 2.0f) * 4.0f, 0.0f, 0.0f);
        }  
      
        void OnGUI()
        {
            moduleEnabled = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 45, 100, 30), moduleEnabled, "Enabled");
            maxSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 85, 100, 30), maxSpeed, 0.0f, 10.0f);
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

