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

#  [ParticleSystem](ParticleSystem.html).Stop

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

## Declaration

public void Stop();

## Declaration

public void Stop(bool withChildren = true);

## Declaration

public void Stop(bool withChildren = true,
[ParticleSystemStopBehavior](ParticleSystemStopBehavior.html) stopBehavior =
ParticleSystemStopBehavior.StopEmitting);

### Parameters

withChildren | Stop all child Particle Systems as well.  
---|---  
stopBehavior | Stop emitting or stop emitting and clear the system.  
  
### Description

Stops playing the Particle System using the supplied stop behaviour.

Additional resources: [Play](ParticleSystem.Play.html),
[Pause](ParticleSystem.Pause.html) functions.  
  
The following example creates a GUI window for manipulating a Particle System.

    
    
    using UnityEngine;  
      
    public class ParticleSystemControllerWindow : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) system
        {
            get
            {
                if (_CachedSystem == null)
                    _CachedSystem = GetComponent<[ParticleSystem](ParticleSystem.html)>();
                return _CachedSystem;
            }
        }
        private [ParticleSystem](ParticleSystem.html) _CachedSystem;  
      
        public [Rect](Rect.html) windowRect = new [Rect](Rect.html)(0, 0, 300, 120);  
      
        public bool includeChildren = true;  
      
        void OnGUI()
        {
            windowRect = [GUI.Window](GUI.Window.html)("ParticleController".GetHashCode(), windowRect, DrawWindowContents, system.name);
        }  
      
        void DrawWindowContents(int windowId)
        {
            if (system)
            {
                [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
                [GUILayout.Toggle](GUILayout.Toggle.html)(system.isPlaying, "Playing");
                [GUILayout.Toggle](GUILayout.Toggle.html)(system.isEmitting, "Emitting");
                [GUILayout.Toggle](GUILayout.Toggle.html)(system.isPaused, "Paused");
                [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();  
      
                [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
                if ([GUILayout.Button](GUILayout.Button.html)("Play"))
                    system.Play(includeChildren);
                if ([GUILayout.Button](GUILayout.Button.html)("Pause"))
                    system.Pause(includeChildren);
                if ([GUILayout.Button](GUILayout.Button.html)("Stop Emitting"))
                    system.Stop(includeChildren, [ParticleSystemStopBehavior.StopEmitting](ParticleSystemStopBehavior.StopEmitting.html));
                if ([GUILayout.Button](GUILayout.Button.html)("Stop & Clear"))
                    system.Stop(includeChildren, [ParticleSystemStopBehavior.StopEmittingAndClear](ParticleSystemStopBehavior.StopEmittingAndClear.html));
                [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();  
      
                includeChildren = [GUILayout.Toggle](GUILayout.Toggle.html)(includeChildren, "Include Children");  
      
                [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
                [GUILayout.Label](GUILayout.Label.html)("[Time](Time.html)(" + system.time + ")");
                [GUILayout.Label](GUILayout.Label.html)("[Particle](ParticleSystem.Particle.html) Count(" + system.particleCount + ")");
                [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
            }
            else
                [GUILayout.Label](GUILayout.Label.html)("No [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html) found");  
      
            [GUI.DragWindow](GUI.DragWindow.html)();
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

