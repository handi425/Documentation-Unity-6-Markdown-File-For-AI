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

# IVisualElementScheduler

interface in UnityEngine.UIElements

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

A scheduler provides the functionality to queue actions to run at a specific
time or duration.

You can use the scheduler to create animations, update the UI, or create tasks
that require a delay or repeated action.  
  
To schedule an action, use the
[IVisualElementScheduler.Execute](UIElements.IVisualElementScheduler.Execute.html)
method. The scheduler runs the action at the next frame.  
  
A [VisualElement](UIElements.VisualElement.html) associates with the
scheduler, which you can access through the
[VisualElement.schedule](UIElements.VisualElement-schedule.html) property. It
returns an
[IVisualElementScheduledItem](UIElements.IVisualElementScheduledItem.html)
interface that provides methods to schedule the action.  
  
For example, you can delay running of the action with the
[IVisualElementScheduledItem.StartingIn](UIElements.IVisualElementScheduledItem.StartingIn.html)
method. You can also specify a condition to unschedule the action with the
[IVisualElementScheduledItem.Until](UIElements.IVisualElementScheduledItem.Until.html)
method.  
  
To repeat the action at a specified interval, use the
[IVisualElementScheduledItem.Every](UIElements.IVisualElementScheduledItem.Every.html)
method. To remove the scheduler, use the
[IVisualElementScheduledItem.Pause](UIElements.IVisualElementScheduledItem.Pause.html)
method.  
  
The scheduler is active only when the VisualElement is attached to a panel.
Detaching the VisualElement from the panel pauses the scheduler, and
reattaching it resumes the scheduler.  
  
Additional resources: [VisualElement.schedule](UIElements.VisualElement-
schedule.html), [VisualElement.panel](UIElements.VisualElement-panel.html),
[IVisualElementScheduledItem](UIElements.IVisualElementScheduledItem.html)  
  

    
    
     // This example uses the scheduler to animate the title logo by changing its background image 
     // to the next frame every 200 milliseconds.
     int m_CurrentTitleLogoFrame = 0;
     public List<[Texture2D](Texture2D.html)> m_TitleLogoFrames = new List<[Texture2D](Texture2D.html)>();
     // Animate title logo.
     var titleLogo = root.Q("menu-title-image");
     titleLogo?.schedule.Execute(() =>
     {
         if (m_TitleLogoFrames.Count == 0)
             return;  
      
             m_CurrentTitleLogoFrame = (m_CurrentTitleLogoFrame + 1) % m_TitleLogoFrames.Count;
             var frame = m_TitleLogoFrames[m_CurrentTitleLogoFrame];
             titleLogo.style.backgroundImage = frame;
     }).Every(200);
    
    
    
     // This example uses the scheduler to animate the scaling of a [VisualElement](UIElements.VisualElement.html).
     [IVisualElementScheduledItem](UIElements.IVisualElementScheduledItem.html) m_AnimationScheduler = null;
     
     public void DoScale()
     {
     // [Scale](UIElements.Scale.html) the [VisualElement](UIElements.VisualElement.html).
     }  
     
     m_AnimationScheduler = this.schedule.Execute(DoScale).Every(1).StartingIn(0);
     
     // Stop the animation
     m_AnimationScheduler.Pause();
    

### Public Methods

[Execute](UIElements.IVisualElementScheduler.Execute.html)|  Schedule this
action to be executed later.  
---|---  
  
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

