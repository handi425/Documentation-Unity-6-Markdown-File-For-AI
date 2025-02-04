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

# AnimationMode

class in UnityEditor

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

[AnimationMode](AnimationMode.html) is used by the
[AnimationWindow](AnimationWindow.html) to store properties modified by the
[AnimationClip](AnimationClip.html) playback.

When exiting [AnimationMode](AnimationMode.html) all properties are reverted
to their default state. Animated properties are also highlighted by the
inspector. Use [StartAnimationMode](AnimationMode.StartAnimationMode.html) to
enter Animation mode. In Animation mode the editor is tinted to show that it
is animating. Properties can be animated via
[SampleAnimationClip](AnimationMode.SampleAnimationClip.html).  
  
The following script example shows how a GameObject can be animated.
[AnimationMode](AnimationMode.html) has functions which support this. The demo
can be launched from the "Examples/AnimationMode demo" menu. Once this demo
starts it requires a GameObject to be selected in the Scene window. (This
example requires the game to not be running in the Game view.) After a
GameObject has been selected the example window will change. Choose a created
animation clip for the chosen GameObject. Once the animation clip has been
loaded the animation can be applied to the GameObject. Clicking the Animate
button adds a slider to the window. Using the slider will apply the animation
to the selected GameObject. The Lock button prevents the animation to be
applied to a different GameObject.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleClass : [EditorWindow](EditorWindow.html)
    {
        protected [GameObject](GameObject.html) go;
        protected [AnimationClip](AnimationClip.html) animationClip;
        protected float time = 0.0f;
        protected bool lockSelection = false;
        protected bool animationMode = false;  
      
        [[MenuItem](MenuItem.html)("Examples/[AnimationMode](AnimationMode.html) demo", false, 2000)]
        public static void DoWindow()
        {
            var window = GetWindowWithRect<ExampleClass>(new [Rect](Rect.html)(0, 0, 300, 80));
            window.Show();
        }  
      
        // Has a [GameObject](GameObject.html) been selection?
        public void OnSelectionChange()
        {
            if (!lockSelection)
            {
                go = [Selection.activeGameObject](Selection-activeGameObject.html);
                Repaint();
            }
        }  
      
        // Main editor window
        public void OnGUI()
        {
            // Wait for user to select a [GameObject](GameObject.html)
            if (go == null)
            {
                [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)("Please select a [GameObject](GameObject.html)", [MessageType.Info](MessageType.Info.html));
                return;
            }  
      
            // Animate and Lock buttons.  Check if Animate has changed
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [GUILayout.Toggle](GUILayout.Toggle.html)([AnimationMode.InAnimationMode](AnimationMode.InAnimationMode.html)(), "Animate");
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
                ToggleAnimationMode();  
      
            [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            lockSelection = [GUILayout.Toggle](GUILayout.Toggle.html)(lockSelection, "Lock");
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();  
      
            // [Slider](UIElements.Slider.html) to use when Animate has been ticked
            [EditorGUILayout.BeginVertical](EditorGUILayout.BeginVertical.html)();
            animationClip = [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(animationClip, typeof([AnimationClip](AnimationClip.html)), false) as [AnimationClip](AnimationClip.html);
            if (animationClip != null)
            {
                float startTime = 0.0f;
                float stopTime  = animationClip.length;
                time = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)(time, startTime, stopTime);
            }
            else if ([AnimationMode.InAnimationMode](AnimationMode.InAnimationMode.html)())
                [AnimationMode.StopAnimationMode](AnimationMode.StopAnimationMode.html)();
            [EditorGUILayout.EndVertical](EditorGUILayout.EndVertical.html)();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (go == null)
                return;  
      
            if (animationClip == null)
                return;  
      
            // Animate the [GameObject](GameObject.html)
            if (![EditorApplication.isPlaying](EditorApplication-isPlaying.html) && [AnimationMode.InAnimationMode](AnimationMode.InAnimationMode.html)())
            {
                [AnimationMode.BeginSampling](AnimationMode.BeginSampling.html)();
                [AnimationMode.SampleAnimationClip](AnimationMode.SampleAnimationClip.html)(go, animationClip, time);
                [AnimationMode.EndSampling](AnimationMode.EndSampling.html)();  
      
                [SceneView.RepaintAll](SceneView.RepaintAll.html)();
            }
        }  
      
        void ToggleAnimationMode()
        {
            if ([AnimationMode.InAnimationMode](AnimationMode.InAnimationMode.html)())
                [AnimationMode.StopAnimationMode](AnimationMode.StopAnimationMode.html)();
            else
                [AnimationMode.StartAnimationMode](AnimationMode.StartAnimationMode.html)();
        }
    }
    

### Static Properties

[animatedPropertyColor](AnimationMode-animatedPropertyColor.html)| The color
used to show that a property is currently being animated.  
---|---  
[candidatePropertyColor](AnimationMode-candidatePropertyColor.html)| The color
used to show that an animated property has been modified.  
[recordedPropertyColor](AnimationMode-recordedPropertyColor.html)| The color
used to show that an animated property automatically records changes in the
animation clip.  
  
### Static Methods

[AddEditorCurveBinding](AnimationMode.AddEditorCurveBinding.html)| Marks a
property defined by an EditorCurveBinding as currently being animated.  
---|---  
[AddPropertyModification](AnimationMode.AddPropertyModification.html)| Marks a
property as currently being animated.  
[BeginSampling](AnimationMode.BeginSampling.html)| Initialise the start of the
animation clip sampling.  
[EndSampling](AnimationMode.EndSampling.html)| Finish the sampling of the
animation clip.  
[InAnimationMode](AnimationMode.InAnimationMode.html)| Checks whether the
Editor is in Animation mode.  
[IsPropertyAnimated](AnimationMode.IsPropertyAnimated.html)| Checks whether
the specified property is in Animation mode and is being animated.  
[SampleAnimationClip](AnimationMode.SampleAnimationClip.html)| Samples the
AnimationClip for the GameObject and also records modified properties when in
Animation mode.  
[SamplePlayableGraph](AnimationMode.SamplePlayableGraph.html)| Samples the
specified output index of a PlayableGraph and also records modified properties
when in Animation mode.  
[StartAnimationMode](AnimationMode.StartAnimationMode.html)| Starts the
Animation mode.  
[StopAnimationMode](AnimationMode.StopAnimationMode.html)| Stops the Animation
mode and reverts any properties that were animated while in Animation mode.  
  
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

