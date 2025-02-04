[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-system-job-system-integration.html)
  * [中文](/cn/current/Manual/particle-system-job-system-integration.html)
  * [日本語](/ja/current/Manual/particle-system-job-system-integration.html)
  * [한국어](/kr/current/Manual/particle-system-job-system-integration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-system-job-system-integration.html)
  * [中文](/cn/current/Manual/particle-system-job-system-integration.html)
  * [日本語](/ja/current/Manual/particle-system-job-system-integration.html)
  * [한국어](/kr/current/Manual/particle-system-job-system-integration.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System optimization](particle-system-optimization.html)
  * Integrate the C# Job System into the Particle System workflow

[](example-particle-system-gpu-instancing-custom-vertex-streams.html)

Example of Particle System GPU instancing with custom vertex streams

[](class-ParticleSystem.html)

Particle System component reference

# Integrate the C# Job System into the Particle System workflow

A **Particle System** A component that simulates fluid entities such as
liquids, clouds and flames by generating and animating large numbers of small
2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can use Unity’s [C# Job
System](job-system.html) to apply custom behaviors to particles.

Unity distributes work from the C# Job System across worker threads, and can
make use of the Burst Compiler. The
[GetParticles()](../ScriptReference/ParticleSystem.GetParticles.html) and
[SetParticles()](../ScriptReference/ParticleSystem.SetParticles.html) methods
offer similar functionality, but run on the main thread and cannot make use of
Unity’s Burst Compiler.

By default, a Particle System job only has access to one or more particles
belonging to that Particle System. Unity passes this data to the job using a
[ParticleSystemJobData](../ScriptReference/ParticleSystemJobs.ParticleSystemJobData.html)
struct. You must pass any other data that the job requires as additional
parameters.

To access particle data, Unity supports the following job types:

##
[IJobParticleSystem](../ScriptReference/ParticleSystemJobs.IJobParticleSystem.html)

This job type executes a single job on a single worker thread. The job has
access to every particle belonging to the Particle System. For example code on
this job type, see the
[IJobParticleSystem.Execute()](../ScriptReference/ParticleSystemJobs.IJobParticleSystem.Execute.html)
Scripting reference.

##
[IJobParticleSystemParallelFor](../ScriptReference/ParticleSystemJobs.IJobParticleSystemParallelFor.html)

This job type executes multiple jobs across multiple worker threads. Each job
can only access the particle at the index specified by the job’s Execute()
function. For example code on this job type, see the
[IJobParticleSystemParallelFor.Execute()](../ScriptReference/ParticleSystemJobs.IJobParticleSystemParallelFor.Execute.html)
Scripting reference.

##
[IJobParticleSystemParallelForBatch](../ScriptReference/ParticleSystemJobs.IJobParticleSystemParallelForBatch.html)

This job type executes multiple jobs across multiple worker threads. Each job
can only access the particles within the range specified by the job’s
Execute() function. For example code on this job type, see the
[IJobParticleSystemParallelForBatch.Execute()](../ScriptReference/ParticleSystemJobs.IJobParticleSystemParallelForBatch.Execute.html)
Scripting reference.

## Burst

As with any other C# job, you can use the Burst Compiler to compile your
particle jobs into highly optimized Burst jobs. For more information, see the
[Burst Compiler
documentation](https://docs.unity3d.com/Packages/com.unity.burst@latest/index.html).

New feature in Unity 2019.3

[](example-particle-system-gpu-instancing-custom-vertex-streams.html)

Example of Particle System GPU instancing with custom vertex streams

[](class-ParticleSystem.html)

Particle System component reference

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

