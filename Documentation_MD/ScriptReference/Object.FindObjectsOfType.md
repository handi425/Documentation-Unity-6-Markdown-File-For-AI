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

#  [Object](Object.html).FindObjectsOfType

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

**Obsolete** Object.FindObjectsOfType has been deprecated. Use
Object.FindObjectsByType instead which lets you decide whether you need the
results sorted or not. FindObjectsOfType sorts the results by InstanceID, but
if you do not need this using FindObjectSortMode.None is considerably faster.

## Declaration

public static Object[] FindObjectsOfType(Type type);

**Obsolete** Object.FindObjectsOfType has been deprecated. Use
Object.FindObjectsByType instead which lets you decide whether you need the
results sorted or not. FindObjectsOfType sorts the results by InstanceID but
if you do not need this using FindObjectSortMode.None is considerably faster.

## Declaration

public static Object[] FindObjectsOfType(Type type, bool includeInactive);

**Obsolete** Object.FindObjectsOfType has been deprecated. Use
Object.FindObjectsByType instead which lets you decide whether you need the
results sorted or not. FindObjectsOfType sorts the results by InstanceID but
if you do not need this using FindObjectSortMode.None is considerably faster.

## Declaration

public static T[] FindObjectsOfType(bool includeInactive);

**Obsolete** Object.FindObjectsOfType has been deprecated. Use
Object.FindObjectsByType instead which lets you decide whether you need the
results sorted or not. FindObjectsOfType sorts the results by InstanceID but
if you do not need this using FindObjectSortMode.None is considerably faster.

## Declaration

public static T[] FindObjectsOfType();

### Parameters

type | The type of object to find.  
---|---  
includeInactive | If true, components attached to inactive GameObjects are also included.  
  
### Returns

**Object[]** The array of objects found matching the type specified.

### Description

Gets a list of all loaded objects of Type `type`.

This does not return assets (such as meshes, textures or prefabs), or objects
with [HideFlags.DontSave](HideFlags.DontSave.html) set. Objects attached to
inactive GameObjects are only included if `inactiveObjects` is set to true.
Use [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html) to
avoid these limitations.  
  
In Editor, this searches the Scene view by default. If you want to find an
object in the Prefab stage, see the
[StageUtility](SceneManagement.StageUtility.html) APIs.  
  
**Note** : This function is very slow. It is not recommended to use this
function every frame. In most cases you can use the singleton pattern instead.  
  
**Obsolete** : This function is obsolete, use
[Object.FindObjectsByType](Object.FindObjectsByType.html) instead. This
replacement allows you to specify whether to sort the resulting array.
FindObjectsOfType() always sorts by InstanceID, so calling
FindObjectsByType(FindObjectsSortMode.InstanceID) produces identical results.
If you specify not to sort the array, the function runs significantly faster,
however, the order of the results can change between calls.

    
    
    using UnityEngine;  
      
    // Ten GameObjects are created and have [TextMesh](TextMesh.html) and
    // [CanvasRenderer](CanvasRenderer.html) components added.
    // When the game runs press the [Space](Space.html) key to display the
    // number of [TextMesh](TextMesh.html) and [CanvasRenderer](CanvasRenderer.html) components.  
      
    public class ScriptExample : [MonoBehaviour](MonoBehaviour.html)
    {
        private const int count = 10;  
      
        void Start()
        {
            var gameObjects = new [GameObject](GameObject.html)[count];
            var expectedTextMeshObjects = new [TextMesh](TextMesh.html)[count];
            var expectedCanvasObjects = new [CanvasRenderer](CanvasRenderer.html)[count];  
      
            for (var i = 0; i < count; ++i)
            {
                gameObjects[i] = new [GameObject](GameObject.html)();
                expectedTextMeshObjects[i] = gameObjects[i].AddComponent<[TextMesh](TextMesh.html)>();
                expectedCanvasObjects[i] = gameObjects[i].AddComponent<[CanvasRenderer](CanvasRenderer.html)>();
            }
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                var foundCanvasObjects = FindObjectsOfType<[CanvasRenderer](CanvasRenderer.html)>();
                var foundTextMeshObjects = FindObjectsOfType(typeof([TextMesh](TextMesh.html)));
                [Debug.Log](Debug.Log.html)(foundCanvasObjects + " : " + foundCanvasObjects.Length);
                [Debug.Log](Debug.Log.html)(foundTextMeshObjects + " : " + foundTextMeshObjects.Length);
            }
        }
    }
    

Additional resources:
[Object.FindObjectsByType](Object.FindObjectsByType.html).

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

