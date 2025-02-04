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

# CrashReport

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Holds data for a single application crash event and provides access to all
gathered crash reports.

If compiled with appropriate settings, Unity will try to gather useful
information, like location and thread stack traces, when your application
crashes. Upon the next application start, if the data gathering was
successful, all crash information will be accessible using this API.  
  
To enable crash report generation, in iOS player settings set "Script Call
Optimization" option to "Fast but no Exceptions". After you build your Xcode
project in Unity, open it and edit trampoline file: Classes/CrashReporter.h.
Change ENABLE_CUSTOM_CRASH_REPORTER define from 0 to 1. Note that the iOS
Player Settings has a Crash Reporting setting with an "Enable CrashReport
API".  
  
Note: this API currently is available only for iOS targets.  
  
Additional resources: [CrashReport.reports](CrashReport-reports.html).

    
    
    using UnityEngine;  
      
    
    // This example shows a list of crash reports (if available),
    // and allows you to output crash data to console, or
    // delete them.
    public class Crashes : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            var reports = [CrashReport.reports](CrashReport-reports.html);
            [GUILayout.Label](GUILayout.Label.html)("Crash reports:");
            foreach (var r in reports)
            {
                [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
                [GUILayout.Label](GUILayout.Label.html)("Crash: " + r.time);
                if ([GUILayout.Button](GUILayout.Button.html)("Log"))
                {
                    [Debug.Log](Debug.Log.html)(r.text);
                }
                if ([GUILayout.Button](GUILayout.Button.html)("Remove"))
                {
                    r.Remove();
                }
                [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
            }
        }
    }
    

### Static Properties

[lastReport](CrashReport-lastReport.html)| Returns last crash report, or null
if no reports are available.  
---|---  
[reports](CrashReport-reports.html)| Returns all currently available reports
in a new array.  
  
### Properties

[text](CrashReport-text.html)| Crash report data as formatted text.  
---|---  
[time](CrashReport-time.html)| Time, when the crash occured.  
  
### Public Methods

[Remove](CrashReport.Remove.html)| Remove report from available reports list.  
---|---  
  
### Static Methods

[RemoveAll](CrashReport.RemoveAll.html)| Remove all reports from available
reports list.  
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

