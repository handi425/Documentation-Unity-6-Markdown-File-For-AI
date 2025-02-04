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
[PlayerConnectionGUIUtility](Networking.PlayerConnection.PlayerConnectionGUIUtility.html).GetConnectionState

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

public static
[Networking.PlayerConnection.IConnectionState](Networking.PlayerConnection.IConnectionState.html)
GetConnectionState([EditorWindow](EditorWindow.html) parentWindow,
Action<string> connectedCallback);

### Parameters

parentWindow | The [EditorWindow](EditorWindow.html) that will use the connection.  
---|---  
connectedCallback | A callback that is fired whenever a user-initiated connection-attempt succeeds.  
  
### Returns

**IConnectionState** Returns the unserialized state of the connection to a
Player, which is used in
[PlayerConnectionGUI.ConnectionTargetSelectionDropdown](Networking.PlayerConnection.PlayerConnectionGUI.ConnectionTargetSelectionDropdown.html)
or
[PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown](Networking.PlayerConnection.PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown.html).
The returned connection state object contains information on what target is
connected to the Player, and what targets are available.

### Description

This method generates a state tracking object for establishing and displaying
an Editor to Player Connection.

This state and the corresponding GUI Methods
([PlayerConnectionGUI.ConnectionTargetSelectionDropdown](Networking.PlayerConnection.PlayerConnectionGUI.ConnectionTargetSelectionDropdown.html)
and
[PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown](Networking.PlayerConnection.PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown.html))
are supposed to be used from within an [EditorWindow](EditorWindow.html). The
supplied Editor Window is used to: 1\. Display an overlay while connecting 2\.
Repaint the window after a connection has been established 3\. Receive
callback calls through connectedCallback when other windows using the same
connection type establish a connection Technically, it might be possible to
supply parentWindow as null and use it outside of
[EditorWindow](EditorWindow.html), but that is neither recommended nor a use-
case we plan to support.  
  
Also keep in mind that the received state is not serialized and needs to be
disposed. The recommended use pattern is to get the state in the
[EditorWindow](EditorWindow.html)'s OnEnable and to dispose of it in
OnDisable.  
  
The connectedCallback will not be fired if, for example, the connection was
made by automatically establishing a profiler connection to a Player or
falling back on to the connection to the Editor. Instead, it only responds to
a user actively choosing a target, and waits until that connection has been
established. If the connection type is one that is shared across Editor
windows, it will also be fired when the user chooses it in a different
[EditorWindow](EditorWindow.html).  
  
The returned state knows what target is currently connected and what targets
are available.

    
    
    using UnityEngine;
    using UnityEngine.Profiling;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.Networking.PlayerConnection;
    using UnityEditor.Networking.PlayerConnection;  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        // The state can survive for the life time of the [EditorWindow](EditorWindow.html) so it's best to store it here and just renew/dispose of it in OnEnable and OnDisable, rather than fetching repeatedly it in OnGUI.
        [IConnectionState](Networking.PlayerConnection.IConnectionState.html) attachProfilerState;  
      
        [[MenuItem](MenuItem.html)("Window/My Window")]
        static void Init()
        {
            MyWindow window = (MyWindow)GetWindow(typeof(MyWindow));
            window.Show();
        }  
      
        private void OnEnable()
        {
            // The state of the connection is not getting serialized and needs to be disposed
            // Therefore, it's recommended to fetch it in OnEnable and call dispose on it in OnDisable
            attachProfilerState = [PlayerConnectionGUIUtility.GetConnectionState](Networking.PlayerConnection.PlayerConnectionGUIUtility.GetConnectionState.html)(this, OnConnected);
        }  
      
        private void OnConnected(string player)
        {
            [Debug.Log](Debug.Log.html)(string.Format("MyWindow connected to {0}", player));
        }  
      
        private void OnGUI()
        {
            // Draw a toolbar across the top of the window and draw the drop-down in the toolbar drop-down style too
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)([EditorStyles.toolbar](EditorStyles-toolbar.html));
            [PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown](Networking.PlayerConnection.PlayerConnectionGUILayout.ConnectionTargetSelectionDropdown.html)(attachProfilerState, [EditorStyles.toolbarDropDown](EditorStyles-toolbarDropDown.html));  
      
            switch (attachProfilerState.connectedToTarget)
            {
                case [ConnectionTarget.None](Networking.PlayerConnection.ConnectionTarget.None.html):
                    //This case can never happen within the [Editor](Editor.html), since the [Editor](Editor.html) will always fall back onto a connection to itself.
                    break;
                case [ConnectionTarget.Player](Networking.PlayerConnection.ConnectionTarget.Player.html):
                    [Profiler.enabled](Profiling.Profiler-enabled.html) = [GUILayout.Toggle](GUILayout.Toggle.html)([Profiler.enabled](Profiling.Profiler-enabled.html), string.Format("Profile the attached Player ({0})", attachProfilerState.connectionName), [EditorStyles.toolbarButton](EditorStyles-toolbarButton.html));
                    break;
                case [ConnectionTarget.Editor](Networking.PlayerConnection.ConnectionTarget.Editor.html):
                    // The name of the [Editor](Editor.html) or the [PlayMode](PlayMode.html) Player would be "[Editor](Editor.html)" so adding the connectionName here would not add anything.
                    [Profiler.enabled](Profiling.Profiler-enabled.html) = [GUILayout.Toggle](GUILayout.Toggle.html)([Profiler.enabled](Profiling.Profiler-enabled.html), "Profile the Player in the [Editor](Editor.html)", [EditorStyles.toolbarButton](EditorStyles-toolbarButton.html));
                    break;
                default:
                    break;
            }
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();
        }  
      
        private void OnDisable()
        {
            // Remember to always dispose the state!
            attachProfilerState.Dispose();
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

