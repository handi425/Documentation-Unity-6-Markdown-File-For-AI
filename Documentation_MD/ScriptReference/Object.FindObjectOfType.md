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

**Method group is Obsolete**  

#  [Object](Object.html).FindObjectOfType

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

[Switch to Manual](../Manual/class-Object.html "Go to Object Component in the
Manual")

**Obsolete** Object.FindObjectOfType has been deprecated. Use
Object.FindFirstObjectByType instead or if finding any instance is acceptable
the faster Object.FindAnyObjectByType.

## Declaration

public static T FindObjectOfType();

**Obsolete** Object.FindObjectOfType has been deprecated. Use
Object.FindFirstObjectByType instead or if finding any instance is acceptable
the faster Object.FindAnyObjectByType.

## Declaration

public static T FindObjectOfType(bool includeInactive);

**Obsolete** Object.FindObjectOfType has been deprecated. Use
Object.FindFirstObjectByType instead or if finding any instance is acceptable
the faster Object.FindAnyObjectByType.

## Declaration

public static Object FindObjectOfType(Type type);

**Obsolete** Object.FindObjectOfType has been deprecated. Use
Object.FindFirstObjectByType instead or if finding any instance is acceptable
the faster Object.FindAnyObjectByType.

## Declaration

public static Object FindObjectOfType(Type type, bool includeInactive);

### Parameters

type | The type of object to find.  
---|---  
  
### Returns

**T** **Object** The first active loaded object that matches the specified
type. It returns null if no Object matches the type.

### Description

Returns the first active loaded object of Type `type`.

Object.FindObjectOfType will not return Assets (meshes, textures, prefabs,
...) or inactive objects. It will not return an object that has
[HideFlags.DontSave](HideFlags.DontSave.html) set.  
  
Please note that this function is very slow. It is not recommended to use this
function every frame. In most cases you can use the singleton pattern instead.  
  
**Obsolete** : This function is obsolete, use
[Object.FindFirstObjectByType](Object.FindFirstObjectByType.html) as a direct
replacement or the faster
[Object.FindAnyObjectByType](Object.FindAnyObjectByType.html) if any object of
the specified type is acceptable.  
  
See Also: [Object.FindFirstObjectByType](Object.FindFirstObjectByType.html),
[Object.FindAnyObjectByType](Object.FindAnyObjectByType.html),
Object.FindObjectsOfType.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Search for any object of Types [TextMesh](TextMesh.html) and [CanvasRenderer](CanvasRenderer.html),
    // if found print the names, else print a message
    // that says that it was not found.
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [TextMesh](TextMesh.html) texture = ([TextMesh](TextMesh.html))FindObjectOfType(typeof([TextMesh](TextMesh.html)));
            if (texture)
                [Debug.Log](Debug.Log.html)("[TextMesh](TextMesh.html) object found: " + texture.name);
            else
                [Debug.Log](Debug.Log.html)("No [TextMesh](TextMesh.html) object could be found");  
      
            [CanvasRenderer](CanvasRenderer.html) canvas = FindObjectOfType<[CanvasRenderer](CanvasRenderer.html)>();
            if (canvas)
                [Debug.Log](Debug.Log.html)("[CanvasRenderer](CanvasRenderer.html) object found: " + canvas.name);
            else
                [Debug.Log](Debug.Log.html)("No [CanvasRenderer](CanvasRenderer.html) object could be found");
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

