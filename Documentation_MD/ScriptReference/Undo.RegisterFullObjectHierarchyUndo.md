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

#  [Undo](Undo.html).RegisterFullObjectHierarchyUndo

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

public static void RegisterFullObjectHierarchyUndo([Object](Object.html)
objectToUndo, string name);

### Parameters

objectToUndo | The object used to determine a hierarchy of objects whose state changes need to be undone.  
---|---  
name | The name of the undo operation.  
  
### Description

Copy the states of a hierarchy of objects onto the undo stack.

This function works similarly to
[Undo.RegisterCompleteObjectUndo](Undo.RegisterCompleteObjectUndo.html). The
key difference is that instead of copying the states of a single object, this
function stores the states of a hierarchy of objects. Depending on the type of
`objectToUndo`, the hierarchy is determined differently:  
  
* If `objectToUndo` is a game object, the hierarchy will contain (a) `objectToUndo` itself and its child game objects; (b) the components attached to these game objects.  
  
* If `objectToUndo` is a component attached to an existing game object, the hierarchy will contain the game object and all of its components, including `objectToUndo`. Child game objects are NOT involved in this case.   
  
* In all other cases, the hierarchy will only contain `objectToUndo` itself. It's then equivalent to calling [Undo.RegisterCompleteObjectUndo](Undo.RegisterCompleteObjectUndo.html) with the same parameters.   
  
If the undo is performed, any changes made to the objects in the above
described hierarchy after this function is called will be undone, and the
objects will be restored to the recorded state.  
  
Transform parent change, AddComponent, and object destruction can not be
restored with this function, for that you should use the dedicated functions.
See [Undo.SetTransformParent](Undo.SetTransformParent.html),
[Undo.AddComponent](Undo.AddComponent.html),
[Undo.DestroyObjectImmediate](Undo.DestroyObjectImmediate.html).  
  
If any object involved is part of the current Scene (e.g. a game object in the
Hierarchy window or a component attached to such game object), calling this
function will immediately mark the Scene as modified, even if you don't
actually change the states of the objects afterwards.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class UndoExamples
    {
        [[MenuItem](MenuItem.html)("[Undo](Undo.html) Examples/RegisterFullObjectHierarchyUndo 1")]
        static void Example1()
        {
            [GameObject](GameObject.html) root = new [GameObject](GameObject.html)("Root");
            [MeshRenderer](MeshRenderer.html) rootComponent1 = root.AddComponent<[MeshRenderer](MeshRenderer.html)>();
            [MeshCollider](MeshCollider.html) rootComponent2 = root.AddComponent<[MeshCollider](MeshCollider.html)>();  
      
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Child");
            child.transform.parent = root.transform;
            [MeshRenderer](MeshRenderer.html) childComponent1 = child.AddComponent<[MeshRenderer](MeshRenderer.html)>();
            [MeshCollider](MeshCollider.html) childComponent2 = child.AddComponent<[MeshCollider](MeshCollider.html)>();  
      
            // Store the states of 'root' and its children.
            [Undo.RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html)(root, "full object hierarchy change");  
      
            root.name = "New Root";
            child.name = "New Child";  
      
            rootComponent1.enabled = false;
            rootComponent2.enabled = false;  
      
            childComponent1.enabled = false;
            childComponent2.enabled = false;  
      
            // If you choose "Edit->[Undo](Undo.html) full object hierarchy change" from the main menu now,
            // the states of both game objects and their components will be restored to what they were right before calling [Undo.RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html).
        }
    }
    
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class UndoExamples
    {
        [[MenuItem](MenuItem.html)("[Undo](Undo.html) Examples/RegisterFullObjectHierarchyUndo 2")]
        static void Example2()
        {
            [GameObject](GameObject.html) root = new [GameObject](GameObject.html)("Root");
            [MeshRenderer](MeshRenderer.html) rootComponent1 = root.AddComponent<[MeshRenderer](MeshRenderer.html)>();
            [MeshCollider](MeshCollider.html) rootComponent2 = root.AddComponent<[MeshCollider](MeshCollider.html)>();  
      
            [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Child");
            child.transform.parent = root.transform;
            [MeshRenderer](MeshRenderer.html) childComponent1 = child.AddComponent<[MeshRenderer](MeshRenderer.html)>();
            [MeshCollider](MeshCollider.html) childComponent2 = child.AddComponent<[MeshCollider](MeshCollider.html)>();  
      
            // Store the states of 'root' and all of its components.
            [Undo.RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html)(rootComponent1, "full object hierarchy change");  
      
            root.name = "New Root";
            child.name = "New Child";  
      
            rootComponent1.enabled = false;
            rootComponent2.enabled = false;  
      
            childComponent1.enabled = false;
            childComponent2.enabled = false;  
      
            // If you choose "Edit->[Undo](Undo.html) full object hierarchy change" from the main menu now,
            // the states of 'root' and all of its components will be restored to what they were right before calling [Undo.RegisterFullObjectHierarchyUndo](Undo.RegisterFullObjectHierarchyUndo.html),
            // but changes made to 'child' and its components won't be restored.
        }
    }
    

* * *

**Obsolete** Use Undo.RegisterFullObjectHierarchyUndo(Object, string) instead.

## Declaration

public static void RegisterFullObjectHierarchyUndo([Object](Object.html)
objectToUndo);

### Description

This overload is deprecated. Use Undo.RegisterFullObjectHierarchyUndo(Object,
string) instead.

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

