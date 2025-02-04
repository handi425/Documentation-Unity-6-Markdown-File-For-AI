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

# ParticleSystemVertexStream

enumeration

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

### Description

All possible Particle System vertex shader inputs.

### Properties

[Position](ParticleSystemVertexStream.Position.html)| The position of each
particle vertex, in world space.  
---|---  
[Normal](ParticleSystemVertexStream.Normal.html)| The vertex normal of each
particle.  
[Tangent](ParticleSystemVertexStream.Tangent.html)| The tangent vector for
each particle (for normal mapping).  
[Color](ParticleSystemVertexStream.Color.html)| The color of each particle.  
[UV](ParticleSystemVertexStream.UV.html)| The first UV stream of each
particle.  
[UV2](ParticleSystemVertexStream.UV2.html)| The second UV stream of each
particle.  
[UV3](ParticleSystemVertexStream.UV3.html)| The third UV stream of each
particle (only for meshes).  
[UV4](ParticleSystemVertexStream.UV4.html)| The fourth UV stream of each
particle (only for meshes).  
[AnimBlend](ParticleSystemVertexStream.AnimBlend.html)| The amount to blend
between animated texture frames, from 0 to 1.  
[AnimFrame](ParticleSystemVertexStream.AnimFrame.html)| The current animation
frame index of each particle.  
[Center](ParticleSystemVertexStream.Center.html)| The center position of the
entire particle, in world space.  
[VertexID](ParticleSystemVertexStream.VertexID.html)| The vertex ID of each
particle.  
[SizeX](ParticleSystemVertexStream.SizeX.html)| The X axis size of each
particle.  
[SizeXY](ParticleSystemVertexStream.SizeXY.html)| The X and Y axis sizes of
each particle.  
[SizeXYZ](ParticleSystemVertexStream.SizeXYZ.html)| The 3D size of each
particle.  
[Rotation](ParticleSystemVertexStream.Rotation.html)| The Z axis rotation of
each particle.  
[Rotation3D](ParticleSystemVertexStream.Rotation3D.html)| The 3D rotation of
each particle.  
[RotationSpeed](ParticleSystemVertexStream.RotationSpeed.html)| The Z axis
rotational speed of each particle.  
[RotationSpeed3D](ParticleSystemVertexStream.RotationSpeed3D.html)| The 3D
rotational speed of each particle.  
[Velocity](ParticleSystemVertexStream.Velocity.html)| The velocity of each
particle, in world space.  
[Speed](ParticleSystemVertexStream.Speed.html)| The speed of each particle,
calculated by taking the magnitude of the velocity.  
[AgePercent](ParticleSystemVertexStream.AgePercent.html)| The normalized age
of each particle, from 0 to 1.  
[InvStartLifetime](ParticleSystemVertexStream.InvStartLifetime.html)| The
reciprocal of the starting lifetime, in seconds (1.0f / startLifetime).  
[StableRandomX](ParticleSystemVertexStream.StableRandomX.html)| A random
number for each particle, which remains constant during their lifetime.  
[StableRandomXY](ParticleSystemVertexStream.StableRandomXY.html)| Two random
numbers for each particle, which remain constant during their lifetime.  
[StableRandomXYZ](ParticleSystemVertexStream.StableRandomXYZ.html)| Three
random numbers for each particle, which remain constant during their lifetime.  
[StableRandomXYZW](ParticleSystemVertexStream.StableRandomXYZW.html)| Four
random numbers for each particle, which remain constant during their lifetime.  
[VaryingRandomX](ParticleSystemVertexStream.VaryingRandomX.html)| A random
number for each particle, which changes during their lifetime.  
[VaryingRandomXY](ParticleSystemVertexStream.VaryingRandomXY.html)| Two random
numbers for each particle, which change during their lifetime.  
[VaryingRandomXYZ](ParticleSystemVertexStream.VaryingRandomXYZ.html)| Three
random numbers for each particle, which change during their lifetime.  
[VaryingRandomXYZW](ParticleSystemVertexStream.VaryingRandomXYZW.html)| Four
random numbers for each particle, which change during their lifetime.  
[Custom1X](ParticleSystemVertexStream.Custom1X.html)| One custom value for
each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom1XY](ParticleSystemVertexStream.Custom1XY.html)| Two custom values for
each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom1XYZ](ParticleSystemVertexStream.Custom1XYZ.html)| Three custom values
for each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom1XYZW](ParticleSystemVertexStream.Custom1XYZW.html)| Four custom values
for each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom2X](ParticleSystemVertexStream.Custom2X.html)| One custom value for
each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom2XY](ParticleSystemVertexStream.Custom2XY.html)| Two custom values for
each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom2XYZ](ParticleSystemVertexStream.Custom2XYZ.html)| Three custom values
for each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[Custom2XYZW](ParticleSystemVertexStream.Custom2XYZW.html)| Four custom values
for each particle, defined by the Custom Data Module, or
ParticleSystem.SetCustomParticleData.  
[NoiseSumX](ParticleSystemVertexStream.NoiseSumX.html)| The accumulated X axis
noise, over the lifetime of the particle.  
[NoiseSumXY](ParticleSystemVertexStream.NoiseSumXY.html)| The accumulated X
and Y axis noise, over the lifetime of the particle.  
[NoiseSumXYZ](ParticleSystemVertexStream.NoiseSumXYZ.html)| The accumulated 3D
noise, over the lifetime of the particle.  
[NoiseImpulseX](ParticleSystemVertexStream.NoiseImpulseX.html)| The X axis
noise on the current frame.  
[NoiseImpulseXY](ParticleSystemVertexStream.NoiseImpulseXY.html)| The X and Y
axis noise on the current frame.  
[NoiseImpulseXYZ](ParticleSystemVertexStream.NoiseImpulseXYZ.html)| The 3D
noise on the current frame.  
[MeshIndex](ParticleSystemVertexStream.MeshIndex.html)| The index of the mesh
used by the current particle.  
[ParticleIndex](ParticleSystemVertexStream.ParticleIndex.html)| The index of
the current particle in the particle data array.  
[ColorPackedAsTwoFloats](ParticleSystemVertexStream.ColorPackedAsTwoFloats.html)|
The color of each particle, packed in a special format to allow decoding on
GPUs that do not support bit-packing operations.  
[MeshAxisOfRotation](ParticleSystemVertexStream.MeshAxisOfRotation.html)| The
axis of rotation used by mesh particles when not using 3D rotation.  
[NextTrailCenter](ParticleSystemVertexStream.NextTrailCenter.html)| The center
of the next trail position, connected to the current position.  
[PreviousTrailCenter](ParticleSystemVertexStream.PreviousTrailCenter.html)|
The center of the previous trail position, connected to the current position.  
[PercentageAlongTrail](ParticleSystemVertexStream.PercentageAlongTrail.html)|
The percentage along the trail, in the range 0-1.  
[TrailWidth](ParticleSystemVertexStream.TrailWidth.html)| The width of the
trail.  
  
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

