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

#  [AnimationMode](AnimationMode.html).IsPropertyAnimated

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

public static bool IsPropertyAnimated([Object](Object.html) target, string
propertyPath);

### Parameters

target | The object to determine if it contained the animation.  
---|---  
propertyPath | The name of the animation to search for.  
  
### Returns

**bool** Whether the property search is found or not.

### Description

Checks whether the specified property is in Animation mode and is being
animated.

[IsPropertyAnimated](AnimationMode.IsPropertyAnimated.html) checks whether a
property is being animated. This check requires also the object where the
property can be found.  
  
`color` is searched for in the following script example . It is part of the
`Renderer` object. Note that the example uses a sphere GameObject and an
animation file, color.anim. The color animation in color.anim has the color
varying from yellow to blue.

    
    
    // Demo showing how IsPropertyAnimated() can be used to determine if a property
    // on an object is being animated. In this example the color in a [Renderer](Renderer.html) is
    // animated.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleClass : [EditorWindow](EditorWindow.html)
    {
        protected [GameObject](GameObject.html) go;
        protected [AnimationClip](AnimationClip.html) animationClip;
        protected float time = 0.0f;
        protected bool showColor = false;  
      
        [[MenuItem](MenuItem.html)("Examples/[AnimationMode](AnimationMode.html) demo")]
        public static void DoWindow()
        {
            var window = GetWindow<ExampleClass>();
            window.Show();
        }  
      
        void OnGUI()
        {
            if (go == null)
            {
                [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)("Select a GO", [MessageType.Info](MessageType.Info.html));
                return;
            }  
      
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("[Color](Color.html) slider");  
      
            if (animationClip == null)
            {
                [AnimationMode.StartAnimationMode](AnimationMode.StartAnimationMode.html)();
                animationClip = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[AnimationClip](AnimationClip.html)>("Assets/color.anim");
            }  
      
            if (animationClip != null)
            {
                float startTime = 0.0f;
                float stopTime  = animationClip.length;
                time = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)(time, startTime, stopTime);
            }  
      
            if (showColor)
            {
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Red color being animated");
            }
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (go == null)
                return;  
      
            if (animationClip == null)
                return;  
      
            if ([AnimationMode.InAnimationMode](AnimationMode.InAnimationMode.html)())
            {
                [Renderer](Renderer.html) rend = go.GetComponent<[Renderer](Renderer.html)>();  
      
                if ([AnimationMode.IsPropertyAnimated](AnimationMode.IsPropertyAnimated.html)(rend, "material._Color.r"))
                {
                    showColor = true;
                }
                else
                {
                    showColor = false;
                }  
      
                [AnimationMode.BeginSampling](AnimationMode.BeginSampling.html)();
                [AnimationMode.SampleAnimationClip](AnimationMode.SampleAnimationClip.html)(go, animationClip, time);
                [AnimationMode.EndSampling](AnimationMode.EndSampling.html)();  
      
                [SceneView.RepaintAll](SceneView.RepaintAll.html)();
            }
        }  
      
        // Has a [GameObject](GameObject.html) been selection?
        public void OnSelectionChange()
        {
            go = [Selection.activeGameObject](Selection-activeGameObject.html);
            Repaint();
        }  
      
        public void OnDestroy()
        {
            [Debug.Log](Debug.Log.html)("Shutting down");
            [AnimationMode.StopAnimationMode](AnimationMode.StopAnimationMode.html)();
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

