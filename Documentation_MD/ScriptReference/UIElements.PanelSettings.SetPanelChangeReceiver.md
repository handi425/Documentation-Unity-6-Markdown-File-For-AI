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

#  [PanelSettings](UIElements.PanelSettings.html).SetPanelChangeReceiver

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

public void
SetPanelChangeReceiver([UIElements.IDebugPanelChangeReceiver](UIElements.IDebugPanelChangeReceiver.html)
value);

### Description

Sets a custom IPanelChangeReceiver in the panelChangeReceiver setter to
receive every change event. This method is available only in development
builds and the editor, as it is a debug feature to go along the profiling of
an application.

Note that the values returned may change over time when the underlying
architecture is modified.  
  
As this is called at every change marked on any visual element of the panel,
the overhead is not negligible. The callback will not be called in release
builds as the method is stripped. The following example uses the
panelChangeReceiver in a game. To test it, add the component to a GameObject
and the Panel Setting asset linked in the component fields.  
  

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class ChangeLogger : [MonoBehaviour](MonoBehaviour.html), [IDebugPanelChangeReceiver](UIElements.IDebugPanelChangeReceiver.html)
    {
        public [PanelSettings](UIElements.PanelSettings.html) panelSettings;
        public bool logChanges = true;
        public bool printOnConsole = false;
        public bool includeStacktrace = true;
        public List<ChangeEntry> changes;
    
        private void OnEnable()
        {
            panelSettings.SetPanelChangeReceiver(this);
        }
    
        public void Initialize()
        {
            changes.Clear();
        }
    
        public void OnVisualElementChange([VisualElement](UIElements.VisualElement.html) element, [VersionChangeType](UIElements.VersionChangeType.html) changeType)
        {
            if (logChanges)
            {
    
                if (changes == null)
                    changes = new List<ChangeEntry>();
    
                changes.Add(new ChangeEntry()
                {
                    changeType = changeType,
                    element = element.ToString(),
                    stackTrace = includeStacktrace ? Environment.StackTrace : null
                });
            }
    
            if (printOnConsole)
            {
                [Debug.Log](Debug.Log.html)($"{string.Join(",", changeType.toStrings()),-40} {element}");
            }
        }
    
        [Serializable]
        public struct ChangeEntry
        {
            public string element;
    
            public [VersionChangeType](UIElements.VersionChangeType.html) changeType;
    
            [TextArea(10, 30)]
            public string stackTrace;
        }
    }
    
    public static class ChangeTypeHelpers
    {
        public static List<string> toStrings(this [VersionChangeType](UIElements.VersionChangeType.html) type)
        {
            var changes = new List<string>();
    
            foreach (var value in ([VersionChangeType](UIElements.VersionChangeType.html)[])Enum.GetValues(typeof([VersionChangeType](UIElements.VersionChangeType.html))))
            {
                if ((type & value) != 0)
                    changes.Add(value.ToString());
            }
            return changes;
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

