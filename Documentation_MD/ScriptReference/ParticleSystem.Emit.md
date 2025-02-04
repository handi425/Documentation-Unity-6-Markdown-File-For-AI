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

#  [ParticleSystem](ParticleSystem.html).Emit

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

public void Emit(int count);

### Parameters

count | Number of particles to emit.  
---|---  
  
### Description

Emit `count` particles immediately.

* * *

## Declaration

public void Emit([ParticleSystem.EmitParams](ParticleSystem.EmitParams.html)
emitParams, int count);

### Parameters

emitParams | Overidden particle properties.  
---|---  
count | Number of particles to emit.  
  
### Description

Emit a number of particles from script.

Setting properties in the emitParams will override those properties in the
emitted particles. Any properties not modified will inherit the behavior
specified in the inspector.

    
    
    using UnityEngine;  
      
    // In this example, we have a [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html) emitting green particles; we then emit and override some properties every 2 seconds.
    public class EmitExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystem](ParticleSystem.html) system;  
      
        void Start()
        {
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Unlit"));  
      
            // Create a green [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var go = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            go.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            system = go.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            go.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var mainModule = system.main;
            mainModule.startColor = [Color.green](Color-green.html);
            mainModule.startSize = 0.5f;  
      
            // Every 2 secs we will emit.
            InvokeRepeating("DoEmit", 2.0f, 2.0f);
        }  
      
        void DoEmit()
        {
            // Any parameters we assign in emitParams will override the current system's when we call Emit.
            // Here we will override the start color and size.
            var emitParams = new [ParticleSystem.EmitParams](ParticleSystem.EmitParams.html)();
            emitParams.startColor = [Color.red](Color-red.html);
            emitParams.startSize = 0.2f;
            system.Emit(emitParams, 10);
            system.Play(); // Continue normal emissions
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

