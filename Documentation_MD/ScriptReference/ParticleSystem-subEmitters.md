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

#  [ParticleSystem](ParticleSystem.html).subEmitters

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
[ParticleSystem.SubEmittersModule](ParticleSystem.SubEmittersModule.html)
subEmitters;

### Description

Script interface for the SubEmittersModule of a Particle System.

The triggering of the child particle emission is linked to events such as the
birth, death and collision of particles in the parent system.  
  
Particle System modules do not need to be reassigned back to the system; they
are interfaces and not independent objects.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // A simple example showing access.
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {  
      
        public [ParticleSystem](ParticleSystem.html) mySubEmitter;  
      
        void Start() {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var sub = ps.subEmitters;
            sub.enabled = true;
            sub.AddSubEmitter(mySubEmitter, [ParticleSystemSubEmitterType.Death](ParticleSystemSubEmitterType.Death.html), [ParticleSystemSubEmitterProperties.InheritNothing](ParticleSystemSubEmitterProperties.InheritNothing.html));
        }
    }
    
    
    using UnityEngine;  
      
    // An example showing how to create 2 [Particle](ParticleSystem.Particle.html) Systems; one as a sub-emitter.
    public class SubEmitterDeathExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start ()
        {
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Unlit"));  
      
            // Create a green [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var rootSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            rootSystemGO.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            var rootParticleSystem = rootSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            rootSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var mainModule = rootParticleSystem.main;
            mainModule.startColor = [Color.green](Color-green.html);
            mainModule.startSize = 0.5f;  
      
            // Create our sub-emitter and set up bursts.
            var subSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var subParticleSystem = subSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            subSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var subMainModule = subParticleSystem.main;
            subMainModule.startColor = [Color.red](Color-red.html);
            subMainModule.startSize = 0.25f;
            var emissionModule = subParticleSystem.emission;
            emissionModule.SetBursts(new [ParticleSystem.Burst](ParticleSystem.Burst.html)[] { new [ParticleSystem.Burst](ParticleSystem.Burst.html)(0.0f, 10) }); // We will emit 10 particles upon death.  
      
            // Set up the sub-emitter.
            subSystemGO.transform.SetParent(rootSystemGO.transform);
            var subEmittersModule = rootParticleSystem.subEmitters;
            subEmittersModule.enabled = true;
            subEmittersModule.AddSubEmitter(subParticleSystem, [ParticleSystemSubEmitterType.Death](ParticleSystemSubEmitterType.Death.html), [ParticleSystemSubEmitterProperties.InheritNothing](ParticleSystemSubEmitterProperties.InheritNothing.html));
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

