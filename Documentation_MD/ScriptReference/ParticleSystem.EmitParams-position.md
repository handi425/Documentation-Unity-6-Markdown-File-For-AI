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

#  [ParticleSystem.EmitParams](ParticleSystem.EmitParams.html).position

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

public [Vector3](Vector3.html) position;

### Description

Override the position of particles this system emits.

When you use this property, the system ignores the Shape module and gives you
direct control over particle spawn positions. To retain the effects of the
Shape module, set [applyShapeToPosition](ParticleSystem.EmitParams-
applyShapeToPosition.html) to true.  
  
Additional resources:
[ParticleSystem.Particle.position](ParticleSystem.Particle-position.html).

    
    
    using UnityEngine;  
      
    // In this example we have a [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html) emitting aligned particles; we then emit and override the position and velocity every 2 seconds.
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) system;  
      
        void Start()
        {
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Unlit"));  
      
            // Create a [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var go = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            go.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            system = go.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            go.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;  
      
            // Every 2 seconds we will emit.
            InvokeRepeating("DoEmit", 2.0f, 2.0f);
        }  
      
        void DoEmit()
        {
            // Any parameters we assign in emitParams will override the current system's when we call Emit.
            // Here we will override the position and velocity. All other parameters will use the behavior defined in the Inspector.
            var emitParams = new [ParticleSystem.EmitParams](ParticleSystem.EmitParams.html)();
            emitParams.position = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
            emitParams.velocity = new [Vector3](Vector3.html)(0.0f, 0.0f, -2.0f);
            system.Emit(emitParams, 1);
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

