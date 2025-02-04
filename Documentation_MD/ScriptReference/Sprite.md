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

# Sprite

class in UnityEngine

/

Inherits from:[Object](Object.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Represents a Sprite object for use in 2D gameplay.

_Sprites_ are 2D graphic objects used for characters, props, projectiles and
other elements of 2D gameplay. The graphics are obtained from bitmap images -
[Texture2D](Texture2D.html). The Sprite class primarily identifies the section
of the image that should be used for a specific Sprite. This information can
then be used by a SpriteRenderer component on a GameObject to actually display
the graphic.  
  
Additional resources: [SpriteRenderer](SpriteRenderer.html) class.

### Properties

[associatedAlphaSplitTexture](Sprite-associatedAlphaSplitTexture.html)|
Returns the Texture that contains the alpha channel from the source Texture.
Unity generates this Texture under the hood for Sprites that have alpha in the
source, and need to be compressed using techniques like ETC1.Returns NULL if
there is no associated alpha Texture for the source Sprite. This is the case
if the Sprite has not been setup to use ETC1 compression.  
---|---  
[border](Sprite-border.html)| Returns the border sizes of the Sprite.  
[bounds](Sprite-bounds.html)|  Bounds of the Sprite, specified by its center
and extents in world space units.  
[packed](Sprite-packed.html)| Returns true if this Sprite is packed in an
atlas.  
[packingMode](Sprite-packingMode.html)| If Sprite is packed (see
Sprite.packed), returns its SpritePackingMode.  
[packingRotation](Sprite-packingRotation.html)| If Sprite is packed (see
Sprite.packed), returns its SpritePackingRotation.  
[pivot](Sprite-pivot.html)| Location of the Sprite's pivot point in the Rect
on the original Texture, specified in pixels.  
[pixelsPerUnit](Sprite-pixelsPerUnit.html)| The number of pixels in the Sprite
that correspond to one unit in world space. (Read Only)  
[rect](Sprite-rect.html)| Location of the Sprite on the original Texture,
specified in pixels.  
[spriteAtlasTextureScale](Sprite-spriteAtlasTextureScale.html)| The Variant
scale of Texture used by the Sprite. This is useful to check when a Variant
SpriteAtlas is being used by Sprites.  
[texture](Sprite-texture.html)| Get the reference to the used Texture. If
packed this will point to the atlas, if not packed will point to the source
Sprite.  
[textureRect](Sprite-textureRect.html)| Get the rectangle this Sprite uses on
its Texture. Raises an exception if this Sprite is tightly packed in an atlas.  
[textureRectOffset](Sprite-textureRectOffset.html)| Gets the offset of the
rectangle this Sprite uses on its Texture to the original Sprite bounds. If
Sprite mesh type is FullRect, offset is zero.  
[triangles](Sprite-triangles.html)| Returns a copy of the array containing
Sprite mesh triangles.  
[uv](Sprite-uv.html)| The base Texture coordinates of the Sprite mesh.  
[vertices](Sprite-vertices.html)| Returns a copy of the array containing
Sprite mesh vertex positions.  
  
### Public Methods

[AddScriptableObject](Sprite.AddScriptableObject.html)| Adds a
ScriptableObject reference to the sprite.  
---|---  
[GetPhysicsShape](Sprite.GetPhysicsShape.html)| Gets a physics shape from the
Sprite by its index.  
[GetPhysicsShapeCount](Sprite.GetPhysicsShapeCount.html)| The number of
physics shapes for the Sprite.  
[GetPhysicsShapePointCount](Sprite.GetPhysicsShapePointCount.html)| Retrieves
the number of points in the selected physics shape for the sprite.  
[GetScriptableObjects](Sprite.GetScriptableObjects.html)| Retrieves an array
of ScriptableObject referenced by the sprite.  
[GetScriptableObjectsCount](Sprite.GetScriptableObjectsCount.html)| Gets the
number of ScriptableObject that the sprite references.  
[GetSecondaryTextureCount](Sprite.GetSecondaryTextureCount.html)| Gets the
number of Secondary Textures that the Sprite is using.  
[GetSecondaryTextures](Sprite.GetSecondaryTextures.html)| Retrieves an array
of SecondarySpriteTexture used by the Sprite.  
[OverrideGeometry](Sprite.OverrideGeometry.html)| Sets up new Sprite geometry.  
[OverridePhysicsShape](Sprite.OverridePhysicsShape.html)| Sets up a new Sprite
physics shape.  
[RemoveScriptableObjectAt](Sprite.RemoveScriptableObjectAt.html)| Removes the
ScriptableObject reference from the sprite.  
[SetScriptableObjectAt](Sprite.SetScriptableObjectAt.html)| Replace the
ScriptableObject reference from the sprite.  
  
### Static Methods

[Create](Sprite.Create.html)| Create a new Sprite object.  
---|---  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

