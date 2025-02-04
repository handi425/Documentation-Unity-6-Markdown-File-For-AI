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

# ShapeModule

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

Script interface for the ShapeModule.

Configures the initial positions and directions of particles.  
  
Additional resources: [ParticleSystem](ParticleSystem.html),
[ParticleSystem.shape](ParticleSystem-shape.html).

### Properties

[alignToDirection](ParticleSystem.ShapeModule-alignToDirection.html)| Align
particles based on their initial direction of travel.  
---|---  
[angle](ParticleSystem.ShapeModule-angle.html)| Angle of the cone to emit
particles from.  
[arc](ParticleSystem.ShapeModule-arc.html)| Angle of the circle arc to emit
particles from.  
[arcMode](ParticleSystem.ShapeModule-arcMode.html)| The mode that Unity uses
to generate particles around the arc.  
[arcSpeed](ParticleSystem.ShapeModule-arcSpeed.html)| In animated modes, this
determines how quickly the particle emission position moves around the arc.  
[arcSpeedMultiplier](ParticleSystem.ShapeModule-arcSpeedMultiplier.html)| A
multiplier of the arc speed of the particle emission shape.  
[arcSpread](ParticleSystem.ShapeModule-arcSpread.html)| Control the gap
between particle emission points around the arc.  
[boxThickness](ParticleSystem.ShapeModule-boxThickness.html)| Thickness of the
box to emit particles from.  
[donutRadius](ParticleSystem.ShapeModule-donutRadius.html)| The thickness of
the Donut shape to emit particles from.  
[enabled](ParticleSystem.ShapeModule-enabled.html)| Specifies whether the
ShapeModule is enabled or disabled.  
[length](ParticleSystem.ShapeModule-length.html)| Length of the cone to emit
particles from.  
[mesh](ParticleSystem.ShapeModule-mesh.html)| Mesh to emit particles from.  
[meshMaterialIndex](ParticleSystem.ShapeModule-meshMaterialIndex.html)| Emit
particles from a single Material of a Mesh.  
[meshRenderer](ParticleSystem.ShapeModule-meshRenderer.html)| MeshRenderer to
emit particles from.  
[meshShapeType](ParticleSystem.ShapeModule-meshShapeType.html)| Where on the
Mesh to emit particles from.  
[meshSpawnMode](ParticleSystem.ShapeModule-meshSpawnMode.html)| The mode to
use to generate particles on a Mesh.  
[meshSpawnSpeed](ParticleSystem.ShapeModule-meshSpawnSpeed.html)| In animated
modes, this determines how quickly the particle emission position moves across
the Mesh.  
[meshSpawnSpeedMultiplier](ParticleSystem.ShapeModule-
meshSpawnSpeedMultiplier.html)| A multiplier of the Mesh spawn speed.  
[meshSpawnSpread](ParticleSystem.ShapeModule-meshSpawnSpread.html)| Control
the gap between particle emission points across the Mesh.  
[normalOffset](ParticleSystem.ShapeModule-normalOffset.html)| Move particles
away from the surface of the source Mesh.  
[position](ParticleSystem.ShapeModule-position.html)| Apply an offset to the
position from which the system emits particles.  
[radius](ParticleSystem.ShapeModule-radius.html)| Radius of the shape to emit
particles from.  
[radiusMode](ParticleSystem.ShapeModule-radiusMode.html)| The mode to use to
generate particles along the radius.  
[radiusSpeed](ParticleSystem.ShapeModule-radiusSpeed.html)| In animated modes,
this determines how quickly the particle emission position moves along the
radius.  
[radiusSpeedMultiplier](ParticleSystem.ShapeModule-
radiusSpeedMultiplier.html)| A multiplier of the radius speed of the particle
emission shape.  
[radiusSpread](ParticleSystem.ShapeModule-radiusSpread.html)| Control the gap
between particle emission points along the radius.  
[radiusThickness](ParticleSystem.ShapeModule-radiusThickness.html)| Radius
thickness of the shape's edge from which to emit particles.  
[randomDirectionAmount](ParticleSystem.ShapeModule-
randomDirectionAmount.html)| Randomizes the starting direction of particles.  
[randomPositionAmount](ParticleSystem.ShapeModule-randomPositionAmount.html)|
Randomizes the starting position of particles.  
[rotation](ParticleSystem.ShapeModule-rotation.html)| Apply a rotation to the
shape from which the system emits particles.  
[scale](ParticleSystem.ShapeModule-scale.html)| Apply scale to the shape from
which the system emits particles.  
[shapeType](ParticleSystem.ShapeModule-shapeType.html)| The type of shape to
emit particles from.  
[skinnedMeshRenderer](ParticleSystem.ShapeModule-skinnedMeshRenderer.html)|
SkinnedMeshRenderer to emit particles from.  
[sphericalDirectionAmount](ParticleSystem.ShapeModule-
sphericalDirectionAmount.html)| Makes particles move in a spherical direction
from their starting point.  
[sprite](ParticleSystem.ShapeModule-sprite.html)| Sprite to emit particles
from.  
[spriteRenderer](ParticleSystem.ShapeModule-spriteRenderer.html)|
SpriteRenderer to emit particles from.  
[texture](ParticleSystem.ShapeModule-texture.html)| Specifies a Texture to
tint the particle's start colors.  
[textureAlphaAffectsParticles](ParticleSystem.ShapeModule-
textureAlphaAffectsParticles.html)| When enabled, the system applies the alpha
channel of the Texture to the particle alpha when the particle spawns.  
[textureBilinearFiltering](ParticleSystem.ShapeModule-
textureBilinearFiltering.html)| When enabled, the system takes four
neighboring samples from the Texture then combines them to give the final
particle value.  
[textureClipChannel](ParticleSystem.ShapeModule-textureClipChannel.html)|
Selects which channel of the Texture to use for discarding particles.  
[textureClipThreshold](ParticleSystem.ShapeModule-textureClipThreshold.html)|
Discards particles when they spawn on an area of the Texture with a value
lower than this threshold.  
[textureColorAffectsParticles](ParticleSystem.ShapeModule-
textureColorAffectsParticles.html)| When enabled, the system applies the RGB
channels of the Texture to the particle color when the particle spawns.  
[textureUVChannel](ParticleSystem.ShapeModule-textureUVChannel.html)| When
using a Mesh as a source shape type, this option controls which UV channel on
the Mesh to use for reading the source Texture.  
[useMeshColors](ParticleSystem.ShapeModule-useMeshColors.html)| Modulate the
particle colors with the vertex colors, or the Material color if no vertex
colors exist.  
[useMeshMaterialIndex](ParticleSystem.ShapeModule-useMeshMaterialIndex.html)|
Emit particles from a single Material, or the whole Mesh.  
  
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

