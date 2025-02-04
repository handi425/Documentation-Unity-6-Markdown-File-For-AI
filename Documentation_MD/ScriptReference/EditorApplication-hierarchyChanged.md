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

#  [EditorApplication](EditorApplication.html).hierarchyChanged

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

Event that is raised when an object or group of objects in the hierarchy
changes.

Actions that trigger this event include creating, renaming, reparenting, or
destroying objects in the current hierarchy, as well as loading, unloading,
renaming, or reordering loaded Scenes. Note that the event is not raised
immediately in response to these actions, but rather during the next update of
the editor application.  
  
Actions taken with objects that have
[HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html) set will not cause
this event to be raised, but changing [Object.hideFlags](Object-
hideFlags.html) will.  
  
The following example script logs the number of objects to the console
whenever the hierarchy changes. Copy it into a file called HierarchyMonitor.cs
and put it in a folder called Editor.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[InitializeOnLoadAttribute](InitializeOnLoadAttribute.html)]
    public static class HierarchyMonitor
    {
        static HierarchyMonitor()
        {
            [EditorApplication.hierarchyChanged](EditorApplication-hierarchyChanged.html) += OnHierarchyChanged;
        }  
      
        static void OnHierarchyChanged()
        {
            var all = [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([GameObject](GameObject.html)));
            var numberVisible =
                all.Where(obj => (obj.hideFlags & [HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html)) != [HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html)).Count();
            [Debug.LogFormat](Debug.LogFormat.html)("There are currently {0} GameObjects visible in the hierarchy.", numberVisible);
        }
    }
    

Additional resources:
[EditorWindow.OnHierarchyChange](EditorWindow.OnHierarchyChange.html).

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

