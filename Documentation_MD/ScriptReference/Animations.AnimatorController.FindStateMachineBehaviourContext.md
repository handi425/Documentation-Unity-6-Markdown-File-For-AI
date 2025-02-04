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

#
[AnimatorController](Animations.AnimatorController.html).FindStateMachineBehaviourContext

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

public static StateMachineBehaviourContext[]
FindStateMachineBehaviourContext([StateMachineBehaviour](StateMachineBehaviour.html)
behaviour);

### Parameters

behaviour | The State Machine Behaviour to get context for.  
---|---  
  
### Returns

**StateMachineBehaviourContext[]** Returns the State Machine Behaviour edition
context.

### Description

Use this function to retrieve the owner of this behaviour.

Please note that this function is very slow. It is not recommended to use this
function every frame. Additional resources:
[StateMachineBehaviourContext](Animations.StateMachineBehaviourContext.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    public class IdleBehaviour : [StateMachineBehaviour](StateMachineBehaviour.html)
    {
        public int transitionCount;
        protected int randomTransitionId = [Animator.StringToHash](Animator.StringToHash.html)("random");  
      
        // OnStateEnter is called when a transition starts and the state machine starts to evaluate the state
        override public void OnStateEnter([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
        }  
      
        // OnStateUpdate is called at each engine tick between OnStateEnter and OnStateExit callback
        override public void OnStateUpdate([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            if (stateInfo.normalizedTime > 0.5f)
                animator.SetInteger(randomTransitionId, [Random.Range](Random.Range.html)(0, transitionCount));
        }  
      
        // OnStateExit is called when a transition ends and the state machine ends to evaluate the state
        override public void OnStateExit([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
        }
    }  
      
    [[CustomEditor](CustomEditor.html)(typeof(IdleBehaviour), true)]
    public class IdleBehaviourEditor : [Editor](Editor.html)
    {
        UnityEditor.Animations.StateMachineBehaviourContext[] context;  
      
        [SerializedProperty](SerializedProperty.html) transitionCount;  
      
        public void OnEnable()
        {
            context = UnityEditor.Animations.AnimatorController.FindStateMachineBehaviourContext(target as [StateMachineBehaviour](StateMachineBehaviour.html));
            if (context != null)
            {
                // animatorObject can be an [AnimatorState](Animations.AnimatorState.html) or [AnimatorStateMachine](Animations.AnimatorStateMachine.html)
                UnityEditor.Animations.AnimatorState state = context[0].animatorObject as UnityEditor.Animations.AnimatorState;
                if (state != null)
                {
                    IdleBehaviour behaviour = target as IdleBehaviour;
                    behaviour.transitionCount = state.transitions.Length;
                }
            }  
      
            transitionCount = serializedObject.FindProperty("transitionCount");
        }  
      
        public override void OnInspectorGUI()
        {
            serializedObject.Update();  
      
            [EditorGUI.BeginDisabledGroup](EditorGUI.BeginDisabledGroup.html)(true);
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(transitionCount);
            [EditorGUI.EndDisabledGroup](EditorGUI.EndDisabledGroup.html)();  
      
            serializedObject.ApplyModifiedProperties();
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

