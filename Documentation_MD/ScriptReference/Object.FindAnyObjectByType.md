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

#  [Object](Object.html).FindAnyObjectByType

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

## Declaration

public static T FindAnyObjectByType();

## Declaration

public static T
FindAnyObjectByType([FindObjectsInactive](FindObjectsInactive.html)
findObjectsInactive);

## Declaration

public static Object FindAnyObjectByType(Type type);

## Declaration

public static Object FindAnyObjectByType(Type type,
[FindObjectsInactive](FindObjectsInactive.html) findObjectsInactive);

### Parameters

type | The type of object to find.  
---|---  
findObjectsInactive | Whether to include components attached to inactive GameObjects. If you don't specify this parameter, this function doesn't include inactive objects in the results.  
  
### Returns

**T** Returns an arbitrary active loaded object that matches the specified
type. If no object matches the specified type, returns null.

### Description

Retrieves any active loaded object of Type `type`.

`Object.FindAnyObjectByType` doesn't return Assets (for example meshes,
textures, or prefabs), or inactive objects. It also doesn't return objects
that have [HideFlags.DontSave](HideFlags.DontSave.html) set.  
  
**Note** : The object that this function returns isn't guaranteed to be the
same between calls, but it is always of the specified type. This function is
faster than [Object.FindFirstObjectByType](Object.FindFirstObjectByType.html)
if you don't need a specific object instance.  
  
See Also: [Object.FindFirstObjectByType](Object.FindFirstObjectByType.html),
[Object.FindObjectsByType](Object.FindObjectsByType.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Search for any object of Types [TextMesh](TextMesh.html) and [CanvasRenderer](CanvasRenderer.html),
    // if found print the names, else print a message
    // that says that it was not found.
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [TextMesh](TextMesh.html) texture = ([TextMesh](TextMesh.html))FindAnyObjectByType(typeof([TextMesh](TextMesh.html)));
            if (texture)
                [Debug.Log](Debug.Log.html)("[TextMesh](TextMesh.html) object found: " + texture.name);
            else
                [Debug.Log](Debug.Log.html)("No [TextMesh](TextMesh.html) object could be found");  
      
            [CanvasRenderer](CanvasRenderer.html) canvas = FindAnyObjectByType<[CanvasRenderer](CanvasRenderer.html)>();
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

