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

#  [Resources](Resources.html).LoadAll

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

public static Object[] LoadAll(string path);

## Declaration

public static Object[] LoadAll(string path, Type systemTypeInstance);

### Parameters

path | Pathname of the target folder. When using the empty string (i.e., ""), the function will load the entire contents of the Resources folder.  
---|---  
systemTypeInstance | Type filter for objects returned.  
  
### Description

Loads all assets in a folder or file at `path` in a Resources folder.

If `path` refers to a folder, all assets in the folder will be returned. If
`path` refers to a file, only that asset will be returned. The `path` is
relative to any Resources folder inside the Assets folder of your project.  
  
**Note:** All asset names and paths in Unity use forward slashes. Paths using
backslashes will **not** work.

    
    
    // Loads all assets in the "[Resources](Resources.html)/Textures" folder
    // Then picks a random one from the list.
    // Note: [Random.Range](Random.Range.html) in this case returns [low,high]
    // range, i.e. the high value is not included in the range.
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private Object[] textures;
        private [GameObject](GameObject.html) go;  
      
        void Start()
        {
            textures = [Resources.LoadAll](Resources.LoadAll.html)("Textures", typeof([Texture2D](Texture2D.html)));  
      
            foreach (var t in textures)
            {
                [Debug.Log](Debug.Log.html)(t.name);
            }  
      
            go = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 70, 150, 30), "Change texture"))
            {
                // change texture on cube
                [Texture2D](Texture2D.html) texture = ([Texture2D](Texture2D.html))textures[[Random.Range](Random.Range.html)(0, textures.Length)];
                go.GetComponent<[Renderer](Renderer.html)>().material.mainTexture = texture;
            }
        }
    }
    

* * *

## Declaration

public static T[] LoadAll(string path);

### Parameters

path | Pathname of the target folder. When using the empty string (i.e., ""), the function will load the entire contents of the Resources folder.  
---|---  
  
### Description

Loads all assets in a folder or file at `path` in a Resources folder.

If `path` refers to a folder, all assets in the folder will be returned. If
`path` refers to a file, only that asset will be returned. Only objects of
type `T` will be returned. The `path` is relative to any Resources folder
inside the Assets folder of your project.  
  
The script example below shows how [LoadAll](Resources.LoadAll.html) can be
used with Linq.

    
    
    // Loads all assets in the "[Resources](Resources.html)/Textures" folder
    // using Linq.
    using UnityEngine;
    using System.Linq;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var textures = [Resources.LoadAll](Resources.LoadAll.html)("Textures", typeof([Texture2D](Texture2D.html))).Cast<[Texture2D](Texture2D.html)>().ToArray();
            foreach (var t in textures)
                [Debug.Log](Debug.Log.html)(t.name);
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

