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

# ReserveModifiersAttribute Constructor

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

public
ReserveModifiersAttribute([ShortcutManagement.ShortcutModifiers](ShortcutManagement.ShortcutModifiers.html)
modifiers);

### Parameters

modifiers | One or more modifiers to reserve.  
---|---  
  
### Description

Creates an attribute that reserves a modifier for a single shortcut.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.ShortcutManagement;
    using UnityEngine;  
      
    public class CustomSceneViewNavigation : ScriptableSingleton<CustomSceneViewNavigation>
    {
        bool moveForward;
        bool moveBack;
        bool boost;  
      
        [ClutchShortcut("Custom [Scene](SceneManagement.Scene.html) Navigation/Move Forward", [KeyCode.KeypadMinus](KeyCode.KeypadMinus.html))]
        [ReserveModifiers([ShortcutModifiers.Shift](ShortcutManagement.ShortcutModifiers.Shift.html))]
        static void MoveForward([ShortcutArguments](ShortcutManagement.ShortcutArguments.html) args)
        {
            instance.moveForward = args.stage == [ShortcutStage.Begin](ShortcutManagement.ShortcutStage.Begin.html);
        }  
      
        [ClutchShortcut("Custom [Scene](SceneManagement.Scene.html) Navigation/Move Back", [KeyCode.KeypadPlus](KeyCode.KeypadPlus.html))]
        [ReserveModifiers([ShortcutModifiers.Shift](ShortcutManagement.ShortcutModifiers.Shift.html))]
        static void MoveBack([ShortcutArguments](ShortcutManagement.ShortcutArguments.html) args)
        {
            instance.moveBack = args.stage == [ShortcutStage.Begin](ShortcutManagement.ShortcutStage.Begin.html);
        }  
      
        private void OnEnable()
        {
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) += DuringSceneGUI;
        }  
      
        private void OnDisable()
        {
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) -= DuringSceneGUI;
        }  
      
        void DuringSceneGUI([SceneView](SceneView.html) view)
        {
            boost = Event.current.shift;  
      
            var speed = boost ? 5 : 1;
            var direction = [Vector3.zero](Vector3-zero.html);  
      
            if (moveForward)
                direction += view.camera.transform.forward;  
      
            if (moveBack)
                direction += -view.camera.transform.forward;  
      
            view.pivot += direction.normalized * [Time.smoothDeltaTime](Time-smoothDeltaTime.html) * speed;
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

