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

# Font

class in UnityEngine

/

Inherits from:[Object](Object.html)

/

Implemented
in:[UnityEngine.TextRenderingModule](UnityEngine.TextRenderingModule.html)

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

Script interface for [font assets](../Manual/class-Font.html).

You can use this class to dynamically switch fonts on Text Meshes.  
  
Additional resources: [TextMesh](TextMesh.html).

### Properties

[ascent](Font-ascent.html)| The ascent of the font.  
---|---  
[characterInfo](Font-characterInfo.html)| Access an array of all characters
contained in the font texture.  
[dynamic](Font-dynamic.html)| Is the font a dynamic font.  
[fontSize](Font-fontSize.html)| The default size of the font.  
[lineHeight](Font-lineHeight.html)| The line height of the font.  
[material](Font-material.html)| The material used for the font display.  
  
### Constructors

[Font](Font-ctor.html)| Create a new Font.  
---|---  
  
### Public Methods

[GetCharacterInfo](Font.GetCharacterInfo.html)| Get rendering info for a
specific character.  
---|---  
[HasCharacter](Font.HasCharacter.html)| Does this font have a specific
character?  
[RequestCharactersInTexture](Font.RequestCharactersInTexture.html)| Request
characters to be added to the font texture (dynamic fonts only).  
  
### Static Methods

[CreateDynamicFontFromOSFont](Font.CreateDynamicFontFromOSFont.html)| Creates
a Font object which lets you render a font installed on the user machine.  
---|---  
[GetMaxVertsForString](Font.GetMaxVertsForString.html)| Returns the maximum
number of verts that the text generator may return for a given string.  
[GetOSInstalledFontNames](Font.GetOSInstalledFontNames.html)| Get names of
fonts installed on the machine.  
[GetPathsToOSFonts](Font.GetPathsToOSFonts.html)| Gets the file paths of the
fonts that are installed on the operating system.  
  
### Events

[textureRebuilt](Font-textureRebuilt.html)| Set a function to be called when
the dynamic font texture is rebuilt.  
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

