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

# SpriteAtlas

class in UnityEngine.U2D

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

Sprite Atlas is an asset created within Unity. It is part of the built-in
sprite packing solution.

A Sprite Atlas stores a list of packable assets. A packable asset is either a
[Sprite](Sprite.html), [Texture2D](Texture2D.html) of
[TextureImporterType.Sprite](TextureImporterType.Sprite.html) or Folder.
Before the packing process begins, these packable assets will be grouped and
traversed to gather all the sprites from them. These will be used in the
packing process. At runtime, these sprites can be enumerated via the Sprite
Atlas (Additional resources:
[SpriteAtlas.GetSprites](U2D.SpriteAtlas.GetSprites.html)).  
  
It also provides dedicated texture settings in the inspector for the packed
texture. The original texture settings of the sprite will have no effect on
the packed texture.  
  
By default, Sprite Atlas will be referenced by the sprite and be available at
runtime. This means that the sprite will be able to acquire the packed texture
from the Sprite Atlas when loaded. A Sprite can be loaded without referencing
any Sprite Atlas. A Sprite loaded this way will render as invisible since
there is no texture. A reference to a Sprite Atlas can be added later.
Additional resources: [SpriteAtlasManager](U2D.SpriteAtlasManager.html).  
  
Sprite Atlas variants can be created by assigning another Sprite Atlas object
as the master. Variants will not repack a new texture from the packable list.
Instead of this, variants will duplicate the master's packed texture and
downscale it according to a user-defined ratio and save this scaled texture.

### Properties

[isVariant](U2D.SpriteAtlas-isVariant.html)| Return true if this SpriteAtlas
is a variant.  
---|---  
[spriteCount](U2D.SpriteAtlas-spriteCount.html)| Get the total number of
Sprite packed into this atlas.  
[tag](U2D.SpriteAtlas-tag.html)| Get the tag of this SpriteAtlas.  
  
### Public Methods

[CanBindTo](U2D.SpriteAtlas.CanBindTo.html)| Return true if Sprite is packed
into this SpriteAtlas.  
---|---  
[GetSprite](U2D.SpriteAtlas.GetSprite.html)| Clone the first Sprite in this
atlas that matches the name packed in this atlas and return it.  
[GetSprites](U2D.SpriteAtlas.GetSprites.html)| Clone all the Sprite in this
atlas and fill them into the supplied array.  
  
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

