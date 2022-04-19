<table>
    <tr>
        <th>功能</th>
        <th>命令</th>
    </tr>
    <tr>
        <td>查看pod</td>
        <td>kubectl --kubeconfig=[kubeconfig] get pod -n [namespace]</td>
    </tr>
    <tr>
        <td>查看pod所在物理机</td>
        <td>kubectl --kubeconfig=[kubeconfig] get pod -n [namespace] -o wide</td>
    </tr>
    <tr>
        <td>查看pod下的container</td>
        <td>kubectl --kubeconfig=[kubeconfig] -n namespace describe pod [pod-name]</td>
    </tr>
    <tr>
        <td>查看日志</td>
        <td>kubectl --kubeconfig=[kubeconfig] -n namespace logs [pod-name] [container-name]</td>
    </tr>
    <tr>
        <td>进入pod</td>
        <td>kubectl --kubeconfig=[kubeconfig] exec -it [pod-name] -n [namespace] /bin/bash</td>
    </tr>
    <tr>
        <td>查看jobs</td>
        <td>kubectl --kubeconfig=[kubeconfig] get jobs -n [namespace]</td>
    </tr>
    <tr>
        <td>查看定时任务</td>
        <td>kubectl --kubeconfig=[kubeconfig]  -n [namespace] get cronjob -o wide<br>
        kubectl --kubeconfig=[kubeconfig]  -n [namespace] describe cronjob [cronjob-name]
        </td>
    </tr>
    <tr>
        <td>删除 pod</td>
        <td>helm --kubeconfig=[kubeconfig] list -n namespace<br>
        helm --kubeconfig=[kubeconfig] uninstall chartname  -n [namespace]<br>
        kubectl --kubeconfig=[kubeconfig] delete pod [podname] -n [namespace]
        </td>
    </tr>
