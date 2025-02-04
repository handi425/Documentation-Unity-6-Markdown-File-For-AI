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

#  [Material](Material.html).parent

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

[Switch to Manual](../Manual/class-Material.html "Go to Material Component in
the Manual")

public [Material](Material.html) parent;

### Description

Parent of this material.

Materials with a non null parent are referred to as material variants.  
  
Material variants will inherit all their properties from their parent, and can
override them on a per property basis. Changing the value of a property of a
material will therefore impact all variants below in the hierarchy.  
  
This property is only available in the Editor, in a built project all material
hierarchies are flattened.  
  
Additional resources: [Material.IsChildOf](Material.IsChildOf.html),
[Material.IsPropertyOverriden](Material.IsPropertyOverriden.html),
[Material.IsPropertyLocked](Material.IsPropertyLocked.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
    #if UNITY_EDITOR
        [[MenuItem](MenuItem.html)("[GameObject](GameObject.html)/Create [Material](Material.html) [Variant](UIElements.ToolbarMenu.Variant.html)")]
        static void DuplicateMaterial()
        {
            [Material](Material.html) selected = [Selection.activeObject](Selection-activeObject.html) as [Material](Material.html);
            if (selected == null)
                return;  
      
            // Create a material variant from selected material
            // And override it's color to red
            [Material](Material.html) material = new [Material](Material.html)(selected);
            material.parent = selected;
            material.color = [Color.red](Color-red.html);  
      
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(material, "Assets/" + selected.name + " Variant.mat");
        }
    #endif
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

