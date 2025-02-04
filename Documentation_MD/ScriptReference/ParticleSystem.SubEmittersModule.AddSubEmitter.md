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
[ParticleSystem.SubEmittersModule](ParticleSystem.SubEmittersModule.html).AddSubEmitter

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

public void AddSubEmitter([ParticleSystem](ParticleSystem.html) subEmitter,
[ParticleSystemSubEmitterType](ParticleSystemSubEmitterType.html) type,
[ParticleSystemSubEmitterProperties](ParticleSystemSubEmitterProperties.html)
properties);

## Declaration

public void AddSubEmitter([ParticleSystem](ParticleSystem.html) subEmitter,
[ParticleSystemSubEmitterType](ParticleSystemSubEmitterType.html) type,
[ParticleSystemSubEmitterProperties](ParticleSystemSubEmitterProperties.html)
properties, float emitProbability);

### Parameters

subEmitter | The sub-emitter to add.  
---|---  
type | The event that creates new particles.  
properties | The properties of the new particles.  
emitProbability | The probability that the sub-emitter emits particles. Accepts values from 0 to 1, where 0 is never and 1 is always.  
  
### Description

Add a new sub-emitter.

Additional resources:
[ParticleSystem.SubEmittersModule.RemoveSubEmitter](ParticleSystem.SubEmittersModule.RemoveSubEmitter.html).

    
    
    using UnityEngine;  
      
    // Add a birth sub-emitter
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Surface"));  
      
            // Create a green [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var rootSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            rootSystemGO.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            var rootParticleSystem = rootSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            rootSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var mainModule = rootParticleSystem.main;
            mainModule.startColor = [Color.green](Color-green.html);
            mainModule.startSize = 0.5f;  
      
            // Spread the particles out more so the sub-emitter effect is more obvious.
            var shapeModule = rootParticleSystem.shape;
            shapeModule.radius = 100;  
      
            // Create our sub-emitter and set up bursts.
            var subSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var subParticleSystem = subSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            subSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var subMainModule = subParticleSystem.main;
            subMainModule.startColor = [Color.red](Color-red.html);
            subMainModule.startSize = 0.25f;
            subMainModule.startLifetime = 0.5f; // very short life particles.
            var emissionModule = subParticleSystem.emission;
            emissionModule.rate = 2; // 1 particle will emit every 0.5 sec.
            emissionModule.SetBursts(new [ParticleSystem.Burst](ParticleSystem.Burst.html)[] // A burst will emit at 1 and 3 secs.
            {
                new [ParticleSystem.Burst](ParticleSystem.Burst.html)(1.0f, 10),
                new [ParticleSystem.Burst](ParticleSystem.Burst.html)(3.0f, 10)
            });  
      
            // Set up the sub particles so they fade over time.
            var colorModule = subParticleSystem.colorOverLifetime;
            colorModule.enabled = true;
            var gradient = new [Gradient](Gradient.html)();
            gradient.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.white](Color-white.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.white](Color-white.html), 1.0f) }, // [Color](Color.html) remains untouched.
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(0.0f, 1.0f) }); // Alpha fades
            colorModule.color = gradient;  
      
            // Setup the sub-emitter.
            subSystemGO.transform.SetParent(rootSystemGO.transform);
            var subEmittersModule = rootParticleSystem.subEmitters;
            subEmittersModule.enabled = true;
            subEmittersModule.AddSubEmitter(subParticleSystem, [ParticleSystemSubEmitterType.Birth](ParticleSystemSubEmitterType.Birth.html), [ParticleSystemSubEmitterProperties.InheritNothing](ParticleSystemSubEmitterProperties.InheritNothing.html));
        }
    }
    
    
    
    using UnityEngine;  
      
    // Add a collision sub-emitter
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // For this example we will need something to collide with in the world.
            var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            cube.transform.position = new [Vector3](Vector3.html)(0, 10, 0); // [Position](UIElements.Position.html) above the [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            cube.transform.localScale = new [Vector3](Vector3.html)(10, 10, 10);  
      
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Surface"));  
      
            // Create a green [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var rootSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            rootSystemGO.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            var rootParticleSystem = rootSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            rootSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var mainModule = rootParticleSystem.main;
            mainModule.startColor = [Color.green](Color-green.html);
            mainModule.startSize = 0.5f;  
      
            // Enable and setup the collisions module.
            var collisionModule = rootParticleSystem.collision;
            collisionModule.enabled = true;
            collisionModule.type = [ParticleSystemCollisionType.World](ParticleSystemCollisionType.World.html);  
      
            // Create our sub-emitter and setup bursts.
            var subSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var subParticleSystem = subSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            subSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var subMainModule = subParticleSystem.main;
            subMainModule.startColor = [Color.red](Color-red.html);
            subMainModule.startSize = 0.25f;
            var emissionModule = subParticleSystem.emission;
            emissionModule.SetBursts(new [ParticleSystem.Burst](ParticleSystem.Burst.html)[] { new [ParticleSystem.Burst](ParticleSystem.Burst.html)(0.0f, 10) }); // We will emit 10 particles upon collision.  
      
            // Set up the sub-emitter.
            subSystemGO.transform.SetParent(rootSystemGO.transform);
            var subEmittersModule = rootParticleSystem.subEmitters;
            subEmittersModule.enabled = true;
            subEmittersModule.AddSubEmitter(subParticleSystem, [ParticleSystemSubEmitterType.Collision](ParticleSystemSubEmitterType.Collision.html), [ParticleSystemSubEmitterProperties.InheritNothing](ParticleSystemSubEmitterProperties.InheritNothing.html));
        }
    }
    
    
    
    using UnityEngine;  
      
    // Add a death sub-emitter
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Surface"));  
      
            // Create a green [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var rootSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            rootSystemGO.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            var rootParticleSystem = rootSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            rootSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var mainModule = rootParticleSystem.main;
            mainModule.startColor = [Color.green](Color-green.html);
            mainModule.startSize = 0.5f;  
      
            // Create our sub-emitter and setup bursts.
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
    
    
    
    using UnityEngine;  
      
    // Add a manual sub-emitter
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        private float m_Timer = 0.0f;
        public float m_Interval = 2.0f;  
      
        void Start()
        {
            // A simple particle material with no texture.
            [Material](Material.html) particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Surface"));  
      
            // Create a green [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
            var rootSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            rootSystemGO.transform.Rotate(-90, 0, 0); // [Rotate](UIElements.Rotate.html) so the system emits upwards.
            ps = rootSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            rootSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var mainModule = ps.main;
            mainModule.startColor = [Color.green](Color-green.html);
            mainModule.startSize = 0.5f;  
      
            // Create our sub-emitter and setup bursts.
            var subSystemGO = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var subParticleSystem = subSystemGO.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            subSystemGO.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;
            var subMainModule = subParticleSystem.main;
            subMainModule.startColor = [Color.red](Color-red.html);
            subMainModule.startSize = 0.25f;
            var emissionModule = subParticleSystem.emission;
            emissionModule.SetBursts(new [ParticleSystem.Burst](ParticleSystem.Burst.html)[] { new [ParticleSystem.Burst](ParticleSystem.Burst.html)(0.0f, 4) }); // We will emit 10 particles when triggered.  
      
            // Set up the sub-emitter.
            subSystemGO.transform.SetParent(rootSystemGO.transform);
            var subEmittersModule = ps.subEmitters;
            subEmittersModule.enabled = true;
            subEmittersModule.AddSubEmitter(subParticleSystem, [ParticleSystemSubEmitterType.Manual](ParticleSystemSubEmitterType.Manual.html), [ParticleSystemSubEmitterProperties.InheritNothing](ParticleSystemSubEmitterProperties.InheritNothing.html));
        }  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            m_Timer += [Time.deltaTime](Time-deltaTime.html);
            while (m_Timer >= m_Interval)
            {
                ps.TriggerSubEmitter(0);
                m_Timer -= m_Interval;
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

