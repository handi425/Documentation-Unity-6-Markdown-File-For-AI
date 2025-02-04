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

#  [Resources](Resources.html).Load

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

Loads the asset of the requested type stored at `path` in a
[Resources](Resources.html) folder.

This method returns the asset at `path` if it can be found, otherwise it
returns null.  
Note that the `path` is case insensitive and must not contain a file
extension. All asset names and paths in Unity use forward slashes, so using
backslashes in the `path` will **not** work.  
  
The `path` is relative to any folder named `Resources` inside the Assets
folder of your project. More than one [Resources](Resources.html) folder can
be used. If you have multiple [Resources](Resources.html) folders you cannot
duplicate the use of an asset name.  
  
For example, a project may have [Resources](Resources.html) folders called
`Assets / Resources/` and `Assets / Guns / Resources/`. The path does not need
to include `Assets` and `Resources` in the string, for example loading a
GameObject at `Assets / Guns / Resources / Shotgun.prefab` would only require
`Shotgun` as the `path`. Also, if `Assets / Resources / Guns / Missiles /
PlasmaGun.prefab` exists it can be loaded using `Guns / Missiles / PlasmaGun`
as the `path` string.  
If you have multiple [Resources](Resources.html) folders you cannot duplicate
the use of an asset name.  
  
If you have multiple assets of different types with the same name, and you
don't specify the type, then the object that Unity returns is non-
deterministic because the potential candidates are not ordered in any
particular way. Instead, use `Resources.Load<T>(path)` to specify the required
asset.

* * *

## Declaration

public static T Load(string path);

### Parameters

path | Path to the target resource to load.  
---|---  
  
### Returns

**T** An object of the requested generic parameter type.

### Description

Loads the asset of the requested type stored at `path` in a
[Resources](Resources.html) folder using a generic parameter type filter of
type `T`.

This method returns the asset at `path` if it can be found and if its type
matches the requested generic parameter type, otherwise it returns null. You
can use this overload to reduce type conversion in your code by providing a
generic type parameter. This allows Unity to perform the C# type conversion
for you.

    
    
    // Loading assets from the [Resources](Resources.html) folder using the generic [Resources.Load](Resources.Load.html)<T>(path) method
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            //Load a text file (Assets/[Resources](Resources.html)/Text/textFile01.txt)
            var textFile = [Resources.Load](Resources.Load.html)<[TextAsset](TextAsset.html)>("Text/textFile01");  
      
            //Load text from a JSON file (Assets/[Resources](Resources.html)/Text/jsonFile01.json)
            var jsonTextFile = [Resources.Load](Resources.Load.html)<[TextAsset](TextAsset.html)>("Text/jsonFile01");
            //Then use [JsonUtility.FromJson](JsonUtility.FromJson.html)<T>() to deserialize jsonTextFile into an object  
      
            //Load a [Texture](Texture.html) (Assets/[Resources](Resources.html)/Textures/texture01.png)
            var texture = [Resources.Load](Resources.Load.html)<[Texture2D](Texture2D.html)>("Textures/texture01");  
      
            //Load a [Sprite](Sprite.html) (Assets/[Resources](Resources.html)/Sprites/sprite01.png)
            var sprite = [Resources.Load](Resources.Load.html)<[Sprite](Sprite.html)>("Sprites/sprite01");  
      
            //Load an [AudioClip](AudioClip.html) (Assets/[Resources](Resources.html)/Audio/audioClip01.mp3)
            var audioClip = [Resources.Load](Resources.Load.html)<[AudioClip](AudioClip.html)>("Audio/audioClip01");
        }
    }
    

* * *

## Declaration

public static Object Load(string path);

## Declaration

public static Object Load(string path, Type systemTypeInstance);

### Parameters

path | Path to the target resource to load.  
---|---  
systemTypeInstance | Type filter for objects returned.  
  
### Returns

**Object** The requested asset returned as an Object.

### Description

Loads an asset stored at `path` in a Resources folder using an optional
`systemTypeInstance` filter.

This method returns the asset at `path` if it can be found and if its type
matches the optional `systemTypeInstance` parameter, otherwise it returns
null.  
You may need to cast the returned object to the actual associated C# type of
the asset in order to access its methods and properties, or use it with other
Unity APIs.

    
    
    // Loading assets from the [Resources](Resources.html) folder using the [Resources.Load](Resources.Load.html)(path)
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Assigns a texture named "Assets/[Resources](Resources.html)/glass" to a [Plane](Plane.html).
        void Start()
        {
            [GameObject](GameObject.html) go = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Plane](PrimitiveType.Plane.html));
            var rend = go.GetComponent<[Renderer](Renderer.html)>();
            rend.material.mainTexture = [Resources.Load](Resources.Load.html)("glass") as [Texture](Texture.html);
        }
    }
    
    
    
    // Loading assets from the [Resources](Resources.html) folder using the [Resources.Load](Resources.Load.html)(path, systemTypeInstance)
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Instantiates a Prefab named "enemy" located in any [Resources](Resources.html) folder in your project's Assets folder.
        void Start()
        {
            [GameObject](GameObject.html) instance = Instantiate([Resources.Load](Resources.Load.html)("enemy", typeof([GameObject](GameObject.html)))) as [GameObject](GameObject.html);
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

