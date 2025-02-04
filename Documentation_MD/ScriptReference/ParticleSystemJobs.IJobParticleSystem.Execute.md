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

#  [IJobParticleSystem](ParticleSystemJobs.IJobParticleSystem.html).Execute

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

## Declaration

public void
Execute([ParticleSystemJobs.ParticleSystemJobData](ParticleSystemJobs.ParticleSystemJobData.html)
jobData);

### Parameters

jobData | Contains the particle properties.  
---|---  
  
### Description

Implement this method to access and modify particle properties.

You can use the following script to attract particles to a supplied position.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.ParticleSystemJobs;  
      
    public class ParticleJob : [MonoBehaviour](MonoBehaviour.html)
    {
        public float effectRange = 2.0f;
        public float effectStrength = 1.0f;
        public float oscillationSpeed = 12.0f;
        public bool useJobSystem = false;  
      
        private float oscillationPhase;  
      
        private [ParticleSystem](ParticleSystem.html) ps;
        private UpdateParticlesJob job = new UpdateParticlesJob();
        private [ParticleSystem.Particle](ParticleSystem.Particle.html)[] mainThreadParticles;  
      
        private static float Remap(float x, float x1, float x2, float y1, float y2)
        {
            var m = (y2 - y1) / (x2 - x1);
            var c = y1 - m * x1;  
      
            return m * x + c;
        }  
      
        private static [Vector3](Vector3.html) CalculateVelocity(ref UpdateParticlesJob job, [Vector3](Vector3.html) delta)
        {
            float attraction = job.effectStrength / job.effectRangeSqr;
            return delta.normalized * attraction;
        }  
      
        private static [Color32](Color32.html) CalculateColor(ref UpdateParticlesJob job, [Vector3](Vector3.html) delta, [Color32](Color32.html) srcColor, UInt32 seed)
        {
            var targetColor = new [Color32](Color32.html)((byte)(seed >> 24), (byte)(seed >> 16), (byte)(seed >> 8), srcColor.a);
            float lerpAmount = delta.magnitude * job.inverseEffectRange;
            lerpAmount = lerpAmount * 0.25f + 0.75f;
            return [Color32.Lerp](Color32.Lerp.html)(targetColor, srcColor, lerpAmount);
        }  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            oscillationPhase = UnityEngine.Random.Range(0.0f, [Mathf.PI](Mathf.PI.html) * 2.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector2](Vector2.html) mouse = [Input.mousePosition](Input-mousePosition.html);
            job.effectPosition = Camera.main.ScreenToWorldPoint(new [Vector3](Vector3.html)(mouse.x, mouse.y, -Camera.main.transform.position.z));
            job.effectRangeSqr = effectRange * effectRange;
            job.effectStrength = effectStrength * Remap([Mathf.Sin](Mathf.Sin.html)(oscillationPhase + [Time.time](Time-time.html) * oscillationSpeed), -1, 1, -1, 0.5f);
            job.inverseEffectRange = (1.0f / effectRange);  
      
            if (!useJobSystem)
            {
                if (mainThreadParticles == null)
                    mainThreadParticles = new [ParticleSystem.Particle](ParticleSystem.Particle.html)[ps.main.maxParticles];  
      
                var count = ps.GetParticles(mainThreadParticles);
                for (int i = 0; i < count; i++)
                {
                    [Vector3](Vector3.html) position = mainThreadParticles[i].position;
                    [Vector3](Vector3.html) delta = position - job.effectPosition;
                    if (delta.sqrMagnitude < job.effectRangeSqr)
                    {
                        mainThreadParticles[i].velocity += CalculateVelocity(ref job, delta);
                        mainThreadParticles[i].startColor = CalculateColor(ref job, delta, mainThreadParticles[i].startColor, mainThreadParticles[i].randomSeed);
                    }
                }
                ps.SetParticles(mainThreadParticles, count);
            }
        }  
      
        void OnParticleUpdateJobScheduled()
        {
            if (useJobSystem)
                job.Schedule(ps);
        }  
      
        struct UpdateParticlesJob : [IJobParticleSystem](ParticleSystemJobs.IJobParticleSystem.html)
        {
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public [Vector3](Vector3.html) effectPosition;  
      
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public float effectRangeSqr;  
      
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public float effectStrength;  
      
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public float inverseEffectRange;  
      
            public void Execute([ParticleSystemJobData](ParticleSystemJobs.ParticleSystemJobData.html) particles)
            {
                var positionsX = particles.positions.x;
                var positionsY = particles.positions.y;
                var positionsZ = particles.positions.z;  
      
                var velocitiesX = particles.velocities.x;
                var velocitiesY = particles.velocities.y;
                var velocitiesZ = particles.velocities.z;  
      
                var colors = particles.startColors;  
      
                var randomSeeds = particles.randomSeeds;  
      
                for (int i = 0; i < particles.count; i++)
                {
                    [Vector3](Vector3.html) position = new [Vector3](Vector3.html)(positionsX[i], positionsY[i], positionsZ[i]);
                    [Vector3](Vector3.html) delta = (position - effectPosition);
                    if (delta.sqrMagnitude < effectRangeSqr)
                    {
                        [Vector3](Vector3.html) velocity = CalculateVelocity(ref this, delta);  
      
                        velocitiesX[i] += velocity.x;
                        velocitiesY[i] += velocity.y;
                        velocitiesZ[i] += velocity.z;  
      
                        colors[i] = CalculateColor(ref this, delta, colors[i], randomSeeds[i]);
                    }
                }
            }
        }
    }
    

You can use the following script with the above example to supply the mouse
position as the point to attract particles towards.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ParticleSpawner : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystem](ParticleSystem.html) prefab;
        public int systemCount = 128;
        public int particleEmissionRatePerSystem = 400;
        public float particleSystemShapeRadius = 1.0f;
        public float totalRadius = 5.0f;
        public float effectRange = 3.0f;
        public float effectStrength = 1.0f;
        public float oscillationSpeed = 10.0f;
        public bool hasTrails = true;
        public bool useJobSystem = false;  
      
        void Start()
        {
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Legacy Shaders/Particles/Additive"));
            material.SetTexture("_MainTex", AssetDatabase.GetBuiltinExtraResource<[Texture2D](Texture2D.html)>("Default-Particle.psd"));  
      
            for (int i = 0; i < systemCount; i++)
            {
                var go = GameObject.Instantiate(prefab);
                var ps = go.GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
                go.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().sharedMaterial = material;  
      
                float x = (float)i / systemCount;
                float theta = x * [Mathf.PI](Mathf.PI.html) * 2;  
      
                var transform = go.GetComponent<[Transform](Transform.html)>();
                transform.position = new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)(theta), [Mathf.Cos](Mathf.Cos.html)(theta), 0.0f) * totalRadius;  
      
                var main = ps.main;
                main.startColor = [Color.HSVToRGB](Color.HSVToRGB.html)(x, [Random.Range](Random.Range.html)(0.5f, 1.0f), [Random.Range](Random.Range.html)(0.5f, 1.0f));  
      
                var emission = ps.emission;
                emission.rateOverTime = particleEmissionRatePerSystem;  
      
                var shape = ps.shape;
                shape.radius = particleSystemShapeRadius;  
      
                var trails = ps.trails;
                trails.enabled = hasTrails;  
      
                var updateJob = go.GetComponent<ParticleJob>();
                updateJob.effectRange = effectRange;
                updateJob.effectStrength = effectStrength;
                updateJob.oscillationSpeed = oscillationSpeed;
                updateJob.useJobSystem = useJobSystem;
            }
        }  
      
        // UI
        void OnGUI()
        {
            float x = 25.0f;
            float y = 60.0f;
            float spacing = 40.0f;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();  
      
            [GUIStyle](GUIStyle.html) backgroundStyle = new [GUIStyle](GUIStyle.html)(GUI.skin.box);
            backgroundStyle.normal.background = [Texture2D.whiteTexture](Texture2D-whiteTexture.html);
            var oldColor = [GUI.backgroundColor](GUI-backgroundColor.html);
            [GUI.backgroundColor](GUI-backgroundColor.html) = new [Color](Color.html)(0.5f, 0.5f, 0.5f, 0.5f);
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(x - 10, y - 35, 260, 230), "[Options](Progress.Options.html)", backgroundStyle);
            [GUI.backgroundColor](GUI-backgroundColor.html) = oldColor;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(x, y, 140, 30), "Effect Range");
            effectRange = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(x + 140, y + 5, 100, 30), effectRange, 0.0f, 10.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(x, y, 140, 30), "Effect Strength");
            effectStrength = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(x + 140, y + 5, 100, 30), effectStrength, 0.0f, 10.0f);
            y += spacing;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(x, y, 140, 30), "Oscillation Speed");
            oscillationSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(x + 140, y + 5, 100, 30), oscillationSpeed, 0.0f, 20.0f);
            y += spacing;  
      
            hasTrails = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(x, y + 5, 140, 30), hasTrails, "[Trails](ParticleSystem.Trails.html)");
            y += spacing;  
      
            useJobSystem = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(x, y + 5, 140, 30), useJobSystem, "Use C# Job [System](Rendering.VirtualTexturing.System.html)");
            y += spacing;  
      
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                ParticleJob[] updateJobs = GameObject.FindObjectsOfType<ParticleJob>();
                for (int i = 0; i < updateJobs.Length; i++)
                {
                    var updateJob = updateJobs[i];
                    updateJob.effectRange = effectRange;
                    updateJob.effectStrength = effectStrength;
                    updateJob.oscillationSpeed = oscillationSpeed;
                    updateJob.useJobSystem = useJobSystem;  
      
                    var ps = updateJob.GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
                    var trails = ps.trails;
                    trails.enabled = hasTrails;
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

